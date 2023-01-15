from django import forms
from .models import MeterReading, EnergyVoucher

class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['submission_date', 'electricity_day', 'electricity_night', 'gas']

        widgets = {
            'submission_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}), 
            'electricity_day': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'electricity_night': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
            'gas': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control'}),
        }

class EnergyVoucherForm(forms.ModelForm):
    class Meta:
        model = EnergyVoucher
        fields = ['code']
