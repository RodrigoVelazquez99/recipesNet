from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(get_profile), name="profile"),
    path('edit_username/', login_required(edit_profile_username), name="edit_profile_username"),
    path('edit_description/', login_required(edit_profile_description), name="edit_description"),
    path('edit_password/', login_required(edit_profile_password), name="edit_password"),
    path('follow/<str:email>/', login_required(follow), name="follow"),
    path('following/', login_required(following), name="following"),
    path('favourites/', login_required(favourites), name="favourite_recipes")
]
