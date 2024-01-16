from django.urls import path
from accounts.views import register

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', register, name='register')
]