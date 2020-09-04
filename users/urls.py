from django.urls import include, path
from django.contrib.auth.decorators import login_required
from main.decorators import chef_required
from .views import *

urlpatterns = [
    path('', chef_required(login_required(get_profile)), name="profile"),
    path('edit_username/', chef_required (login_required(edit_profile_username)), name="edit_profile_username"),
    path('edit_description/', chef_required (login_required(edit_profile_description)), name="edit_description"),
    path('edit_password/', chef_required (login_required(edit_profile_password)), name="edit_password"),
    path('follow/<str:email>/', chef_required (login_required(follow)), name="follow"),
    path('following/', chef_required (login_required(following)), name="following"),
    path('favourites/', chef_required (login_required(favourites)), name="favourite_recipes")
]
