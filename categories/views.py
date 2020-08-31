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
