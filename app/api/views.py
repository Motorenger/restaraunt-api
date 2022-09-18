from rest_framework.decorators import api_view
from rest_framework.response import Response

from restaurants.models import Restaurant


@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(['POST'])
def uploadImage(request):
    data = request.data

    obj_id = data['obj_id']
    obj= Restaurant.objects.get(id=obj_id)
    print(request.FILES.get('image'))
    obj.daily_menu = request.FILES.get('image')
    obj.save()

    return Response('Image was uploaded')
