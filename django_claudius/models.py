from django import forms
from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db.models import CASCADE


class Case(models.Model):
    # Input
    name = models.CharField('Client Name', max_length=200, default='')
    age = models.IntegerField('Client Age', null=True)
    hospital_bill = models.FloatField('Hospital Bill', null=True)

    # Output
    prediction = models.DecimalField('Case Value', null=True, decimal_places=2, max_digits=10)

    # Dev-only
    owner = models.ForeignKey(User, on_delete=CASCADE, null=True)
