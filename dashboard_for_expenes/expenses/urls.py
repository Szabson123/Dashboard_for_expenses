from django.urls import path
from expenses.views import AddEarnigs, AddExpenses, AllDashboards, DetailDashboardPage, CreateDashboard

urlpatterns = [
    path('main_page/', AllDashboards.as_view(), name='main_page'),
    path('dashboard/<int:pk>/', DetailDashboardPage.as_view(), name='dashboard'),
    path('dashboard_form/', CreateDashboard.as_view(), name='createdashboard'),

    path('dashboard/<int:dashboard_id>/add_earning/', AddEarnigs.as_view(), name='earnings_form_without_directorie'),
    path('dashboard/<int:dashboard_id>/directorie/<int:directorie_id>/add_earning/', AddEarnigs.as_view(),
         name='earnings_form_with_directorie'),

    path('dashboard/<int:dashboard_id>/add_expenses/', AddExpenses.as_view(), name='expenses_form_without_directorie'),
    path('dashboard/<int:dashboard_id>/directorie/<int:directorie_id>/add_expenses/', AddExpenses.as_view(),
         name='expenses_form_with_directorie'),
]