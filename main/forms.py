from django import forms
from database.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import check_password

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

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()

    # Check if email exists and password is correct
    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not User.objects.filter(email=email):
            raise ValidationError ("No existe un usuario con ese email")
            return cleaned_data
        user = User.objects.get(email=email)
        if not user.check_password(password):
            raise ValidationError ("El password no es valido")
        return cleaned_data
