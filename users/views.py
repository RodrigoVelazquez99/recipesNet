from django.shortcuts import render, redirect
from django.http import JsonResponse
from database.models import Chef

# Create your views here.

def get_profile(request):
    user = request.user
    chef = user.chef
    return render (request, 'users/profile.html', {'chef' : chef})

# Update the username of current chef
def edit_profile_username(request):
    new_username = request.POST.get('new_username')
    user = request.user
    repeated_username = False
    if new_username != user.username:
        if Chef.objects.filter(user__username=new_username).exclude(user=user):
            repeated_username = True
        else:
            chef = Chef.objects.get(user=user)
            chef.user.username = new_username
            chef.user.save()
            chef.save()
    data = {
        'content' : {
            'repeated_username' :repeated_username,
            'redirect_url' : '/profile'
        }
    }
    return JsonResponse(data)

# Save the new description
def edit_profile_description(request):
    user = request.user
    new_description = request.POST.get('new_description')
    chef = user.chef
    chef.description = new_description
    chef.save()
    return redirect('/profile')

# Save the new password
def edit_profile_password(request):
    user = request.user
    new_password = request.POST.get('password')
    user.set_password(new_password)
    user.save()
    return redirect('/logout')

# Get the chefs that current chef follow
def following(request):
    user = request.user
    chef = user.chef
    followees = chef.followees.all()
    return render(request, 'users/following.html', {'followees' : followees})

# Follow the chef
def follow(request, email):
    user = request.user
    chef = user.chef
    other = Chef.objects.get(user__email=email)
    chef.follow_chef(other)
    return redirect("/profile/following/")

# Get the recipes wich the chef likes
def favourites(request):
    user = request.user
    chef = user.chef
    recipes = chef.recipe_likes.all()
    return render (request, 'users/favourite_recipes.html', {'recipes' : recipes})
