from django.urls import path
from expenses.views import (AddEarnigs, AddExpenses,
                            AllDashboards, DetailDashboardPage,
                            CreateDashboard, CreateDirectorie,
                            EarningsUpdateView, EarningsDeleteView,
                            ExpenseUpdateView, ExpenseDeleteView)

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

    path('dashboard/<int:dashboard_id>/directorie/create/', CreateDirectorie.as_view(), name='create_directorie'),
    path('earnings/edit/<int:pk>/', EarningsUpdateView.as_view(), name='edit_earnings'),
    path('earnings/delete/<int:pk>/', EarningsDeleteView.as_view(), name='delete_earnings'),

    path('expenses/edit/<int:pk>/', ExpenseUpdateView.as_view(), name='edit_expenses'),
    path('expenses/delete/<int:pk>/', ExpenseDeleteView.as_view(), name='delete_expenses'),
]