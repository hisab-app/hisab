from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ExpenseGroup(models.Model):
    description=models.CharField(max_length=100,blank=False)
    members=models.ManyToManyField(User)
    def __str__(self):
        return self.description

class ExpenseItem(models.Model):
    description=models.CharField(max_length=100,blank=False)
    amount=models.FloatField(default=0)
    expense_group=models.ForeignKey(ExpenseGroup)
    author=models.ForeignKey(User)
    def __str__(self):
        return self.description