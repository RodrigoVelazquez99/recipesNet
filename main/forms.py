from django import forms
from database.models import User

class SignUpForm(forms.Form):
    email = forms.EmailField()
    username = forms.CharField()
    password = forms.CharField()
    description = forms.CharField()

    # Check if email and username is unique
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        username = cleaned_data.get('username')
        if User.objects.filter(email=email):
            self.add_error("email", "Ya existe un usuario con el mismo correo")
        if User.objects.filter(username=username):
            self.add_error("username", "Ya existe un usuario con el mismo nombre")
        return cleaned_data
