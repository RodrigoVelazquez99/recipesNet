from django.shortcuts import render, redirect
from database.models import Category
from django.http import JsonResponse
from .forms import *

# Create your views here.

# Get all categories
def get_categories(request):
    form = CategoryForm()
    categories = Category.objects.all()
    return render(request, "categories/categories.html", {"categories" : categories, "form" : form})

# Save the new category or return an error flag if exists a category with the same name.
def new_category(request):
    name = request.POST.get('name')
    if Category.objects.filter(name=name):
        repeated_category = True
        print ('repetido')
    else:
        Category.objects.create(name=name)
        repeated_category = False
        print ('ok')
    data = {
        'content' : {
            'repeated_category' :repeated_category,
            'redirect_url' : '/categories'
        }
    }
    return JsonResponse(data)

# Edit the given category
def edit_category(request):
    new_name = request.POST.get('new_name')
    old_name = request.POST.get('old_name')
    if new_name == old_name:
        repeated_category = False
    else:
        if Category.objects.filter(name=new_name):
            repeated_category = True
        else:
            edited = Category.objects.get(name=old_name)
            edited.name = new_name
            edited.save()
            repeated_category = False
    data = {
        'content' : {
            'repeated_category' : repeated_category,
            'redirect_url' : '/categories'
        }
    }
    return JsonResponse(data)
