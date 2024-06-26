from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label = 'Email address', help_text = 'Your email address.')
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']