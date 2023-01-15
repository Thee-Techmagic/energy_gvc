from django import forms
from .models import MeterReading, EnergyVoucher

class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['submission_date', 'electricity_day', 'electricity_night', 'gas']

class EnergyVoucherForm(forms.ModelForm):
    class Meta:
        model = EnergyVoucher
        fields = ['code']
