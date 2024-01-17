
from typing import Any
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from base.models import Expense, User, Earnings
from base.forms import AddEarinings, AddExpenses


from django.db.models import Sum

class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'expenses/main_page.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        total_expenses = Expense.objects.filter(user=self.request.user).aggregate(Sum('cost'))['cost__sum'] or 0
        total_earnigs = Earnings.objects.filter(user=self.request.user).aggregate(Sum('money'))['money__sum'] or 0
        
        context['total_earnigs'] = total_earnigs
        context['total_expenses'] = total_expenses
        
        context['balance'] = total_earnigs - total_expenses
        
        context["expenses"] = Expense.objects.filter(user=self.request.user)
        context["earnings"] = Earnings.objects.filter(user=self.request.user)
        return context


class AddEarnigs(LoginRequiredMixin, CreateView):
    model = Earnings
    form_class = AddEarinings
    template_name = 'expenses/earnings_form.html'
    success_url = '/expenses/main_page/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
class AddExpenses(LoginRequiredMixin, CreateView):
    template_name = 'expenses/expenses_form.html'
    success_url = '/expenses/main_page/'
    model = Expense
    form_class = AddExpenses
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)