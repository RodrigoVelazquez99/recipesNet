from django.forms import forms, ModelForm
from database.models import Recipe
from database.models import Category

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        exclude = ['id_recipe', 'likes', 'owner', 'coments']
