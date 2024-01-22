from django import forms

from django.contrib.auth.forms import UserCreationForm

from base.models import Profile, Expense, User, Earnings, Dashboard, Directorie


class UserRegisterForm(UserCreationForm):
    
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
        

class AddEarnings(forms.ModelForm):
    
    class Meta:
        model = Earnings
        fields = ['name', 'money',]
        

class AddExpenses(forms.ModelForm):

    class Meta:
        model = Expense        
        fields = ['name', 'cost',]
        

class AddDashboard(forms.ModelForm):
    
    class Meta:
        model = Dashboard        
        fields = ['name', 'target']
        

class AddDirectorie(forms.ModelForm):
    dashboard = forms.ModelChoiceField(
        queryset=Dashboard.objects.all(),
        empty_label="Wybierz dashboard",
        label="Dashboard"
    )
    
    class Meta:
        model = Directorie
        fields = ['name', 'amount', 'dashboard', ]
