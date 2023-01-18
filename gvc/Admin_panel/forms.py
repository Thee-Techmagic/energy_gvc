from django import forms
from core.models import MeterReading

class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['meter_reading_day', 'meter_reading_night', 'meter_reading_gas']
        
        