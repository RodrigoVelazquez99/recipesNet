from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from main.decorators import chef_required
from .views import *

urlpatterns = [
    path('new/', chef_required (login_required(new_post)), name="new_post"),
    path('delete/<int:id_post>', chef_required (login_required(delete_post)), name="delete_post"),
    path('share/<int:id_post>', chef_required (login_required(share_post)), name="share_post"),
    path('like/<int:id_post>', chef_required (login_required(like_post)), name="like_post"),
    path('coment/<int:id_post>', chef_required (login_required(coment_post)), name="coment_post")
]
