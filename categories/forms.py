from django.forms import forms, ModelForm
from database.models import Category

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = ['recipes_category']
