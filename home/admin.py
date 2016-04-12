from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(ExpenseItem)
admin.site.register(ExpenseGroup)