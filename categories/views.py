from django.shortcuts import render, redirect
from database.models import Category
# Create your views here.

def get_categories(request):
    categories = Category.objects.all()
    return render(request, "categories/categories.html", {"categories" : categories})
