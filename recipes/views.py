from django.shortcuts import render, redirect
from django.http import HttpResponse
from database.models import Recipe
from database.models import Chef
from database.models import Category
from .forms import RecipeForm

# Create your views here.

# Get all recipes of current chef
def get_recipes(request):
    form = RecipeForm()
    user = request.user
    chef = Chef.objects.get(user=user)
    recipes = Recipe.objects.filter(owner=chef)
    categories = Category.objects.all()
    return render (request, "recipes/recipes.html", {"recipes" : recipes, "form" : form, "categories" : categories})

# Create a new recipe
def new_recipe(request):
    if request.method == "POST":
        user = request.user
        chef = Chef.objects.get(user=user)
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = chef
            recipe.save()
            return redirect("/recipes")
        else:
            raise Exception ("Ocurrio un error con el formulario")
    return redirect("/recipes")

# Show menu to edit recipes or delete
def edit_recipes(request):
    user = request.user
    chef = Chef.objects.get(user=user)
    recipes = Recipe.objects.filter(owner=chef)
    return render (request, "recipes/recipes_edit.html", {"recipes" : recipes})

# Delete the recipe by it's id
def delete_recipe(request, id_recipe):
    deleted = Recipe.objects.get(pk=id_recipe)
    deleted.delete()
    return redirect("/recipes/edit")
