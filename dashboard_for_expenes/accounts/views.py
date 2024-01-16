from django.shortcuts import render, redirect

from django.contrib.auth import login
from base.forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_page')
    else:
        form=UserRegisterForm()
        
    return render(request, 'accounts/register.html', {'form' : form})
            
            
