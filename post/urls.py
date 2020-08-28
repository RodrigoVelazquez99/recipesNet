from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('new/', login_required(new_post), name="new_post"),
    path('delete/<int:id_post>', login_required(delete_post), name="delete_post"),
    path('share/<int:id_post>', login_required(share_post), name="share_post")
]
