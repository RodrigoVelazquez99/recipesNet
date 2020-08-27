from django.forms import forms, ModelForm
from database.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['id_post', 'date', 'publisher', 'sharers']
