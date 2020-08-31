from django.urls import path
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from main.decorators import admin_required
from .views import *

urlpatterns = [
    path('', login_required(admin_required(get_categories)), name='categories'),
    path('new/', login_required(admin_required(new_category)), name='new_category'),
    path('edit/', login_required(admin_required(edit_category)), name="edit_category")
]
