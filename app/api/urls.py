from django.urls import path 

from .views import create_rest, upload_votemenu

urlpatterns = [
    path("restaurant/create/", create_rest, name="create_rest"),

    path('upload-votemenu/', upload_votemenu, name="upload_votemenu"),
]