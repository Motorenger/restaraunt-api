from django.urls import path 

from .views import hello_world, uploadImage

urlpatterns = [
    path("", hello_world, name="home"),
    path('upload/', uploadImage, name="image-upload"),
]