from ipaddress import v6_int_to_packed
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from restaurants.models import VoteMenus, Restaurant
from restaurants.serializers import RestMenuSerializer, VoteMenuSerializer

@api_view(['POST'])
def create_restaurant(request):
    data = request.data

    restaurant = Restaurant.objects.create(name=data['name'])

    return Response('Restaurant Created Successfully')



@api_view(['POST'])
def upload_votemenu(request):
    data = request.data

    rest_id = data['rest_id']
    restaurant = Restaurant.objects.get(id=rest_id)

    vote_menu = VoteMenus.objects.create(restaurant=restaurant, menu=data["vote_menu"])

    vote_menu.save()
    return Response('Image was uploaded', content_type="image/jpg")



class CurrentMenuView(APIView):

    def get_restaurant(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404


    def get(self, request):
        restaurant = self.get_restaurant(request.user.restaurant.id)
        print(restaurant)
        serializer = RestMenuSerializer(restaurant, context={'request': request})

        return Response(serializer.data)


class VoteMenusView(APIView):
    def get_restaurant(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404


    def get(self, request):
        restaurant = self.get_restaurant(request.user.restaurant.id)
        vote_menus = VoteMenus.objects.filter(restaurant=restaurant)
        print(restaurant)
        serializer = VoteMenuSerializer(vote_menus, context={'request': request}, many=True)

        return Response(serializer.data)


@api_view(["PUT"])
def vote_for_menu(request):
    menu_id = request.data["menu_id"]
    menu_obj  = VoteMenus.objects.get(id=menu_id)
    menu_obj.votes+=1
    menu_obj.save()
    serialzer = VoteMenuSerializer(menu_obj, context={'request': request})

    return Response(serialzer.data)


@api_view(["GET"])
def vote_results(request):
    restaurant = request.user.restaurant
    try:
        restaurant = Restaurant.objects.get(pk=restaurant.id)
    except Restaurant.DoesNotExist:
        raise Http404
    
    vote_menus = VoteMenus.objects.filter(restaurant=restaurant)

    winner = vote_menus[0]
    for menu in vote_menus[1:]:
        if menu.votes > winner.votes:
            winner = menu
        else:
            menu.delete()
    
    serialzer = VoteMenuSerializer(winner, context={'request': request})
    restaurant.daily_menu = winner.menu
    restaurant.save()
    winner.delete()
    return Response(serialzer.data)
