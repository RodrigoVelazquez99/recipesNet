from django.shortcuts import render, redirect
from database.models import Chef

# Create your views here.

def get_profile(request):
    user = request.user
    chef = Chef.objects.get(user=user)
    return render (request, 'users/profile.html', {'chef' : chef})
