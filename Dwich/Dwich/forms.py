from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    class Meta:
        email = forms.EmailField(max_length=100, required=True, help_text='Inform a valid email adress')
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # nom et prenom ?