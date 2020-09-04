from django.urls import path
from django.contrib.auth.decorators import login_required
from main.decorators import chef_required
from .views import *

urlpatterns = [
    path('', chef_required (login_required(get_recipes)), name='recipes'),
    path('new/', chef_required (login_required(new_recipe)), name='add_recipe'),
    path('edit/', chef_required (login_required(edit_recipes)), name='edit_recipes'),
    path('delete/<int:id_recipe>', chef_required (login_required(delete_recipe)), name='delete_recipe'),
    path('edit/<int:id_recipe>', chef_required (login_required(edit_recipe)), name='edit_recipe'),
    path('<int:id_recipe>/', chef_required (login_required(get_recipe)), name='get_recipe'),
    path('coment/', chef_required (login_required(coment_recipe)), name="coment_recipe"),
    path('like/<int:id_recipe>', chef_required (login_required(like_recipe)), name="like_recipe")
]
