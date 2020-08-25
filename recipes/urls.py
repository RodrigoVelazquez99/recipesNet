from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', login_required(views.get_recipes), name='recipes'),
    path('new/', login_required(views.new_recipe), name='add_recipe'),
    path('edit/', login_required(views.edit_recipes), name='edit_recipes'),
    path('delete/<int:id_recipe>', login_required(views.delete_recipe), name='delete_recipe'),
    path('edit/<int:id_recipe>', login_required(views.edit_recipe), name='edit_recipe')
]
