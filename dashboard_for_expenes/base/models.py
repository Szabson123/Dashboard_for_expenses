from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username


class Dashboard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    target = models.DecimalField(max_digits=30, decimal_places=2)
    data = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Directorie(models.Model):
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE, related_name='directories', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class Expense(models.Model):
    name = models.CharField(max_length=255)
    cost = models.DecimalField(max_digits=15, decimal_places=2)
    descripton = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    directorie = models.ForeignKey(Directorie, on_delete=models.CASCADE, related_name='expenses', null=True)
    
    def __str__(self):
        return self.name
    
 
class Earnings(models.Model):
    name = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dashboard = models.ForeignKey(Dashboard, on_delete=models.CASCADE)
    directorie = models.ForeignKey(Directorie, on_delete=models.CASCADE, related_name='expenses', null=True)
    
    def __str__(self):
        return self.name
    

