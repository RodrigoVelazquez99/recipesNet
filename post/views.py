from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from database.models import Chef
from database.models import Recipe
from .forms import *
# Create your views here.

def home(request):
    user = request.user
    chef = Chef.objects.get(user=user)
    list_post = chef.refresh_post()
    form = PostForm()
    recipes = Recipe.objects.filter(owner=chef)
    return render (request, 'post/home.html', {"list_post" : list_post, "form" : form, "recipes" : recipes})

# Create a new post
def new_post(request):
    if request.method == "POST":
        user = request.user
        chef = Chef.objects.get(user=user)
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publisher = chef
            post.save()
            return redirect ('/home')