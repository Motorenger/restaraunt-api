from django.urls import path 

from .views import (create_restaurant, upload_votemenu, vote_for_menu, 
                    vote_results, CurrentMenuView, VoteMenusView)

urlpatterns = [
    path("restaurant/create/", create_restaurant, name="create_rest"),
    path("current-menu/", CurrentMenuView.as_view(), name="current_menu"),
    path("vote-menus/", VoteMenusView.as_view(), name="vote_menus"),
    path("vote-for-menu/", vote_for_menu, name="vote_for_menu"),
    path("vote-results/", vote_results, name="vote_results"),


    path('upload-votemenu/', upload_votemenu, name="upload_votemenu"),
]