from django.urls import include, path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(get_profile), name="profile")
]
