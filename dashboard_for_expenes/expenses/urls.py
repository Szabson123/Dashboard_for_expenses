from django.urls import path
from expenses.views import AddEarnigs, AddExpenses, AllDashboards, DetailDashboardPage, CreateDashboard

urlpatterns = [
    path('main_page/', AllDashboards.as_view(), name='main_page'),
    path('dashboard/<int:pk>/', DetailDashboardPage.as_view(), name='dashboard'),
    path('dashboard_form/', CreateDashboard.as_view(), name='createdashboard'),
    
    path('dashboard/<int:pk>/add_earning/', AddEarnigs.as_view(), name='earnings_form'),
    path('dashboard/<int:pk>/add_expense/', AddExpenses.as_view(), name='expenses_form'),

]