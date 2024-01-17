from django import forms

from django.contrib.auth.forms import UserCreationForm

from base.models import Profile, Expense, User, Earnings

class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        

class AddEarinings(forms.ModelForm):
    
    class Meta:
        model = Earnings
        fields = ['name', 'money', 'description']
        

class AddExpenses(forms.ModelForm):
    
    class Meta:
        model = Expense        
        fields = ['name', 'cost', 'descripton']