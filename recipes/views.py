from django.shortcuts import render, redirect
from django.http import HttpResponse
from database.models import Recipe
from database.models import Chef
from database.models import Category
from database.models import IngredientsRecipe
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
    deleted.image.delete()
    deleted.delete()
    return redirect("/recipes/edit")

def edit_recipe(request, id_recipe):
    user = request.user
    chef = Chef.objects.get(user=user)
    recipe = Recipe.objects.get(id_recipe=id_recipe)
    ingredients = recipe.ingredients.all()
    ingredients_name = [i.ingredient for i in ingredients]
    if request.method == "POST":
        list_ingredients = request.POST.getlist('ingredient')
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            edit_recipe = form.save(commit=False)
            recipe.name = edit_recipe.name
            recipe.image.delete()
            recipe.image = edit_recipe.image
            recipe.description = edit_recipe.description
            recipe.category = edit_recipe.category
            deleted_ingredients = list(set(ingredients_name) - set(list_ingredients))
            recipe.delete_ingredients(deleted_ingredients)
            list_ingredients = list(set(list_ingredients) - set(ingredients_name))
            recipe.add_ingredients(list_ingredients)
            recipe.save()
            return redirect("/recipes/edit")
    else:
        form = RecipeForm()
    return render (request, "recipes/recipe_edit.html", {"recipe" : recipe, "ingredients_recipe" : ingredients, "form" : form})
