from django import forms

from django.contrib.auth.forms import UserCreationForm

from base.models import Profile, Expense, User

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        