from django.contrib import admin
from base import models


admin.site.register(models.Expense)
admin.site.register(models.Profile)
admin.site.register(models.Earnings)