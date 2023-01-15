
import datetime
from django.db import models
#import user model
from django.contrib.auth.models import User
class MeterReading(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateField(default=datetime.date.today)
    electricity_day = models.DecimalField(max_digits=10, decimal_places=2)
    electricity_night = models.DecimalField(max_digits=10, decimal_places=2)
    gas = models.DecimalField(max_digits=10, decimal_places=2)

class Bill(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bill_date = models.DateField(default=datetime.date.today)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

class EnergyVoucher(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=8, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    redeemed = models.BooleanField(default=False)
