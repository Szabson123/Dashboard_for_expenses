from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Expense(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=15, decimal_places=6)
    descripton = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
    
class Earnings(models.Model):
    name = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name