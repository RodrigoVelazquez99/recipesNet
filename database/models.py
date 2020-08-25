from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, username):
        if not email:
            raise ValueError(_('Email necesario'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username):
        user = self.create_user(email, password, username)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        return user

class User(AbstractUser):
    email = models.EmailField(max_length=40, primary_key=True, unique=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    def __str__(self):
        return self.username

    def __eq__(self, other):
        if isinstance (other, User) and self.email == other.email:
            return True
        return False

    class Meta:
        db_table = "user"

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.name

    def __eq__(self, other):
        if isinstance (other, Admin) and self.user == other.user:
            return True
        return False

    class Meta:
        db_table = "admin"

class Chef(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()
    followers = models.ManyToManyField("self", through="Follow", symmetrical=False,
                                        through_fields=('to_chef','from_chef'),
                                        related_name="followees")
    def __eq__(self, other):
        if isinstance (other, Chef) and self.user == other.user:
            return True
        return False

    def __str__(self):
        return self.user.name

    # Follow another chef or unfollow if is followed already.
    # other : the Chef to follow
    # return True if follow or False if unfollow.
    def follow_chef(self, other):
        if not Follow.objects.filter(to_chef=other, from_chef=self):
            Follow.objects.create(to_chef=other, from_chef=self)
            return True
        else:
            Follow.objects.filter(to_chef=other, from_chef=self).delete()
        return False

    # Create a post
    def create_post(self, description, recipe_published):
        Post.objects.create(description=description, publisher=self, recipe_published=recipe_published)

    # Return all post to see, order by date in descending order
    def refresh_post(self):
        list_post = []
        posters = Post.objects.all().order_by('-date')
        for post in posters:
            if post.publisher == self:
                list_post.append(post)

            if post in self.shared_post.all():
                list_post.append(post)

            for followee in self.followees.all():
                if post.publisher == followee:
                    list_post.append(post)
                shares = post.sharers.all()
                if followee in shares:
                    list_post.append(post)

        return list_post

    # Share a post
    def share_post(self, post):
        post.sharers.add(self)

    class Meta:
        db_table = "chef"

class Follow(models.Model):
    to_chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name="to_chef")
    from_chef = models.ForeignKey(Chef, on_delete=models.CASCADE, related_name="from_chef")

    def __str__(self):
        return '{} follows {}'.format(self.to_chef, self.from_chef)

    def __eq__(self, other):
        if isinstance (other, Follow) and self.to_chef == other.to_chef and self.from_chef == other.from_chef:
            return True
        return False

    class Meta:
        db_table = "follow"
        unique_together = (("to_chef", "from_chef"),)

class Category(models.Model):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Category) and self.name == other.name:
            return True
        return False

    class Meta:
        db_table = "category"

class Recipe(models.Model):
    id_recipe = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="recipe_img/")
    description = models.TextField()
    likes = models.ManyToManyField(Chef, related_name="recipe_likes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(Chef, on_delete=models.CASCADE)
    coments = models.ManyToManyField(Chef, related_name="recipes_coments", through="Coment")

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance (other, Recipe) and self.id_recipe == other.id_recipe:
            return True
        return False

    def __hash__(self):
        return super().__hash__()

    # Add like or unlike is has like.
    # chef : Chef who likes the recipe.
    # return True if like or False if unlike
    def add_like(self, chef):
        if chef not in self.likes.all():
            self.likes.add(chef)
            return True
        else:
            self.likes.remove(chef)
        return False

    # Add coment.
    # chef : Chef who coment the recipe.
    # msg : the coment.
    def add_coment(self, chef, msg):
        Coment.objects.create(recipe=self, chef=chef, message=msg)

    # Add ingredient.
    # ingredient : Ingredient to add.
    def add_ingredient(self, ingredient):
        IngredientsRecipe.objects.create(ingredient=ingredient, recipe=self)

    # Delete all ingredients in the list from the recipe
    def delete_ingredients(self, list):
        for delete in list:
            IngredientsRecipe.objects.filter(ingredient=delete, recipe=self).delete()

    # Add new ingredients in the recipe
    def add_ingredients(self, list):
        for new in list:
            IngredientsRecipe.objects.create(ingredient=new, recipe=self)

    class Meta:
        db_table = "recipe"

class IngredientsRecipe(models.Model):
    ingredient = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.ingredient

    def __eq__(self, other):
        if isinstance (other, IngredientsRecipe) and self.recipe == other.recipe and  self.ingredient == other.ingredient:
            return True
        return False

    class Meta:
        db_table = "ingredients_recipe"
        unique_together = (('recipe','ingredient'),)

class Coment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_coments")
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)

    def __str__(self):
        return self.message

    def __eq__(self, other):
        if isinstance (other, Coment) and self.recipe == other.recipe and self.chef == other.chef and self.message == other.message:
            return True
        return False

    class Meta:
        db_table = "coment"

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    publisher = models.ForeignKey(Chef, on_delete=models.CASCADE)
    recipe_published = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    sharers = models.ManyToManyField(Chef, related_name="shared_post")
    def __str__(self):
        return self.description

    def __eq__(self, other):
        if isinstance (other, Post) and self.id_post == other.id_post:
            return True
        return False

    class Meta:
        db_table = "post"
