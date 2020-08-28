from django.contrib.auth import login, authenticate, logout, get_user_model
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from django.template import loader
from database.models import Chef
from database.models import Recipe

# Create your views here.


def index(request):
    if not request.user.is_authenticated:
        return render(request, "main/index.html")
    return redirect("/home")

# Return recipes and chef that have coincidences with the query
def search(request):
    if request.method == "GET":
        query = request.GET['query']
        recipes = Recipe.objects.filter(name__istartswith=query)
        chefs = Chef.objects.filter(user__username__istartswith=query)
    return render(request, "main/search.html", {"query" : query, "recipes" : recipes, "chefs" : chefs})

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
