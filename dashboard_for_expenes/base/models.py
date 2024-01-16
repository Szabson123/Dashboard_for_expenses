from django.db import models
from datetime import datetime


class Expense(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=15, decimal_places=6)
    descripton = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name
    
