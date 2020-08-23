from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.get_recipes), name='recipes'),
    path('new/', login_required(views.new_recipe), name='add_recipe'),
    path('edit/', login_required(views.edit_recipes), name='edit_recipes')
]
