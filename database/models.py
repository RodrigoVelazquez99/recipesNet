from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=40, primary_key=True, unique=True)
    name = models.CharField(max_length=40)
    password = models.TextField()
    class Meta:
        db_table = "user"

class Admin(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    class Meta:
        db_table = "admin"

class Chef(models.Model):
    email = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()
    followers = models.ManyToManyField("self", related_name="followees", symmetrical=False)
    class Meta:
        db_table = "chef"

class Category(models.Model):
    name = models.CharField(max_length=30, primary_key=True)
    class Meta:
        db_table = "category"

class Recipe(models.Model):
    id_recipe = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to="recipe_img/")
    description = models.TextField()
    likes = models.ManyToManyField(Chef, related_name="recipes_likes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(Chef, on_delete=models.CASCADE)
    coments = models.ManyToManyField(Chef, related_name="recipes_coments", through="Coment")
    class Meta:
        db_table = "recipe"

class IngredientsRecipe(models.Model):
    ingredient = models.CharField(max_length=20)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    class Meta:
        db_table = "ingredients_recipe"
        unique_together = (('recipe','ingredient'),)

class Coment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    class Meta:
        db_table = "coment"

class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    description = models.TextField()
    publisher = models.ForeignKey(Chef, on_delete=models.CASCADE)
    recipe_published = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    sharers = models.ManyToManyField(Chef, related_name="shared_post")
    class Meta:
        db_table = "post"
