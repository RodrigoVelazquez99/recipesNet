from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('', login_required(get_recipes), name='recipes'),
    path('new/', login_required(new_recipe), name='add_recipe'),
    path('edit/', login_required(edit_recipes), name='edit_recipes'),
    path('delete/<int:id_recipe>', login_required(delete_recipe), name='delete_recipe'),
    path('edit/<int:id_recipe>', login_required(edit_recipe), name='edit_recipe'),
    path('<int:id_recipe>/', login_required(get_recipe), name='get_recipe'),
    path('coment/', login_required(coment_recipe), name="coment_recipe"),
    path('like/<int:id_recipe>', login_required(like_recipe), name="like_recipe")
]
