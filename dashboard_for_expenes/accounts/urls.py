from django.urls import path
from expenses.views import Expenses

urlpatterns = [
    path('', LoginView.as_view(), name='main_page'),
    
]