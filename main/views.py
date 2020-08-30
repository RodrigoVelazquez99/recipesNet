from django.contrib.auth import login, authenticate, logout, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.template import loader
from database.models import Chef
from database.models import Recipe
from database.models import Category

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "main/index.html")
    return redirect("/home")

# Return recipes and chef that have coincidences with the query
def search(request):
    if request.method == "GET":
        user = request.user
        query = request.GET['query']
        recipes = Recipe.objects.filter(name__istartswith=query)
        chefs = Chef.objects.filter(user__username__istartswith=query).exclude(user__username=user.username)
    return render(request, "main/search.html", {"query" : query, "recipes" : recipes, "chefs" : chefs})

# Follow the chef
def follow(request, email):
    user = request.user
    chef = Chef.objects.get(user=user)
    other = Chef.objects.get(user__email=email)
    chef.follow_chef(other)
    return redirect("/")

# Get all recipes to see
def explore(request, category):
    if category == "all":
        recipes = Recipe.objects.all()
        category_selected = "Todas las categorias"
    else:
        category_selected = Category.objects.get(name=category)
        recipes = Recipe.objects.filter(category=category_selected)
        category_selected = category_selected.name
    categories = Category.objects.all()
    return render (request, "main/explore.html", {"recipes" : recipes, "categories" : categories, "category_selected" : category_selected})



def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            description = form.cleaned_data.get('description')
            password = form.cleaned_data.get('password')
            User = get_user_model()
            user = User.objects.create_user(email=email, username=username, password=password)
            chef = Chef.objects.create(user=user, description=description)
            login(request, user)
            return redirect("/home")
    else:
        form = SignUpForm()

    return render(request, "main/signup.html", {"form":form})

def login_(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            User = get_user_model()
            user = User.objects.get(email=email)
            login(request, user)
            return redirect("/home")
    else:
        form = LoginForm()
    return render(request, "main/login.html", {"form":form})

def logout_(request):
    logout(request)
    return redirect("/")
