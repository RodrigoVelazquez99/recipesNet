from django.shortcuts import render, redirect
from django.http import JsonResponse
from database.models import Recipe
from .forms import *
# Create your views here.

def home(request):
    user = request.user
    chef = user.chef
    list_post = chef.refresh_post()
    form = PostForm()
    recipes = Recipe.objects.filter(owner=chef)
    context = {
        "list_post" : list_post,
        "form" : form,
        "recipes" : recipes,
        "chef" : chef
    }
    return render (request, 'post/home.html', context)

# Create a new post
def new_post(request):
    if request.method == "POST":
        user = request.user
        chef = user.chef
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.publisher = chef
            post.save()
            return redirect ('/home')

# Delete the post by id and the post that were shared by it.
def delete_post(request, id_post):
    deleted = Post.objects.get(id_post=id_post)
    Post.objects.filter(publisher=deleted.publisher, original_post=deleted).delete()
    deleted.delete()
    return redirect ('/home')

# Share the post by id
def share_post(request, id_post):
    user = request.user
    chef = user.chef
    shared = Post.objects.get(id_post=id_post)
    chef.share_post(shared)
    return redirect ('/home')

# Like the post by id
def like_post(request, id_post):
    user = request.user
    chef = user.chef
    post = Post.objects.get(id_post=id_post)
    flag = post.add_like(chef)
    likes_count = post.likes.count()
    post.save()
    data = {
        'content' : {
            'flag' : flag,
            'likes_count' : likes_count
        }
    }
    return JsonResponse(data)

# Get coments of the post by id or create a new coment
def coment_post(request, id_post):
    if request.method == 'GET':
        post = Post.objects.get(id_post=id_post)
        coments = post.post_coments.all().values()
        data = {
            'content' : {
                'coments' : list(coments)
            }
        }
        return JsonResponse(data)
    else:
        post = Post.objects.get(id_post=id_post)
        new_coment = request.POST.get('coment')
        user = request.user
        chef = user.chef
        post.add_coment(chef=chef, msg=new_coment)
        post.save()
        return JsonResponse({'ok' : True})
