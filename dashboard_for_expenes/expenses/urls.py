from django.urls import path
from expenses.views import Expenses

urlpatterns = [
    path('main_page/', Expenses.as_view(), name='main_page'),
    
]