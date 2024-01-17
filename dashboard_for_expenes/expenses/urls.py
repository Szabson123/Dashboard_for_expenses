from django.urls import path
from expenses.views import MainPage


urlpatterns = [
    path('main_page/', MainPage.as_view(), name='main_page'),
    
]