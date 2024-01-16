from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from base.models import Expense


class Expenes(ListView):
    model = Expense
    context_object_name = 'expenses'
    template_name = 'expenses/main_page'
    
    def get_queryset(self):
        return Expense.objects.all()