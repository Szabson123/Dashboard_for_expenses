from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from base.models import Expense, User, Earnings

from django.db.models import Sum

class MainPage(LoginRequiredMixin, TemplateView):
    template_name = 'expenses/main_page.html'
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        total_expenses = Expense.objects.filter(user=self.request.user).aggregate(Sum('cost'))['cost__sum'] or 0
        total_earnigs = Earnings.objects.filter(user=self.request.user).aggregate(Sum('money'))['money__sum'] or 0
        
        context['balance'] = total_earnigs - total_expenses
        
        context["expenses"] = Expense.objects.filter(user=self.request.user)
        context["earnings"] = Earnings.objects.filter(user=self.request.user)
        return context
