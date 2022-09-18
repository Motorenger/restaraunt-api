from rest_framework.decorators import api_view
from rest_framework.response import Response

from restaurants.models import Restaurant, VoteMenus


@api_view(['POST'])
def create_rest(request):
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
    return Response('Image was uploaded')
