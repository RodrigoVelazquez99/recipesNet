from django.shortcuts import render, redirect
from django.http import JsonResponse
from database.models import Chef

# Create your views here.

def get_profile(request):
    user = request.user
    chef = Chef.objects.get(user=user)
    return render (request, 'users/profile.html', {'chef' : chef})

# Update the username of current chef
def edit_profile_username(request):
    new_username = request.POST.get('new_username')
    old_username = request.POST.get('old_username')
    repeated_username = False
    if new_username != old_username:
        if Chef.objects.filter(user__username=new_username):
            repeated_username = True
        else:
            user = request.user
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
    chef = Chef.objects.get(user=user)
    chef.description = new_description
    chef.save()
    return redirect('/profile')
