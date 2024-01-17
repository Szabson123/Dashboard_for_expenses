from django.urls import path
from expenses.views import MainPage, AddEarnigs, AddExpenses

urlpatterns = [
    path('main_page/', MainPage.as_view(), name='main_page'),
    path('earnings_form/', AddEarnigs.as_view(), name='earnings_form'),
    path('expenses_form/', AddExpenses.as_view(), name='expenses_form')
]