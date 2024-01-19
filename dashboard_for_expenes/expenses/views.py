
from typing import Any

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, TemplateView, CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

from base.models import Expense, User, Earnings, Dashboard, Directorie
from base.forms import AddEarinings, AddExpenses, AddDashboard, AddDirectorie


from django.db.models import Sum


class AllDashboards(LoginRequiredMixin, ListView):
    model = Dashboard
    template_name = 'expenses/main_page.html'

    def get_queryset(self):
        return Dashboard.objects.filter(user=self.request.user)


class CreateDashboard(LoginRequiredMixin, CreateView):
    model = Dashboard
    template_name = 'expenses/dashboard_create_form.html'
    form_class = AddDashboard
    success_url = '/expenses/main_page/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class DetailDashboardPage(LoginRequiredMixin, DetailView):
    model = Dashboard
    template_name = 'expenses/detail_dashboard_page.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        dashboard = self.get_object()
        
        total_expenses = Expense.objects.filter(user=self.request.user).aggregate(Sum('cost'))['cost__sum'] or 0
        total_earnigs = Earnings.objects.filter(user=self.request.user).aggregate(Sum('money'))['money__sum'] or 0
        
        context['dashboard_id'] = self.kwargs.get('pk')
        context['total_earnigs'] = total_earnigs
        context['total_expenses'] = total_expenses
        
        context['balance'] = total_earnigs - total_expenses
        context['target'] = dashboard.target
        
        context["expenses"] = Expense.objects.filter(user=self.request.user)
        context["earnings"] = Earnings.objects.filter(user=self.request.user)
        return context


class AddEarnigs(LoginRequiredMixin, CreateView):
    model = Earnings
    form_class = AddEarinings
    template_name = 'expenses/earnings_form.html'

    def form_valid(self, form):
        dashboard_id = self.kwargs.get('dashboard_id')
        dashboard = get_object_or_404(Dashboard, pk=dashboard_id, user=self.request.user)

        form.instance.user = self.request.user
        form.instance.dashboard = dashboard

        directorie_id = self.kwargs.get('directorie_id')
        if directorie_id:
            directorie = get_object_or_404(Directorie, pk=directorie_id, user=self.request.user)
            form.instance.directorie = directorie

        return super().form_valid(form)

    def get_success_url(self) -> str:
        dashboard_id = self.kwargs.get('dashboard_id')
        return reverse('dashboard', kwargs={'pk': dashboard_id})


class AddExpenses(LoginRequiredMixin, CreateView):
    template_name = 'expenses/expenses_form.html'
    model = Expense
    form_class = AddExpenses
    
    def form_valid(self, form):
        
        dashboard_id = self.kwargs.get('dashboard_id')
        directorie_id = self.kwargs.get('directorie_id')
        
        dashboard = get_object_or_404(Dashboard, pk=dashboard_id, user=self.request.user)
        directorie = get_object_or_404(Directorie, pk=directorie_id, user=self.request.user)

        form.instance.user = self.request.user
        form.instance.dashboard = dashboard
        form.instance.directorie = directorie
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        dashboard_id = self.kwargs.get('dashboard_id')
        return reverse('dashboard',  kwargs={'dashboard_pk': dashboard_id})
    

class CreateDirectiorie(LoginRequiredMixin, CreateView):
    template_name = 'expenses/directorie_form.html'
    model = Directorie
    form_class = AddDirectorie
    success_url = '/expenses/main_page/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)