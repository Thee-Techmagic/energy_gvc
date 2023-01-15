#import render 
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def Admin_login(request):
    return render(request, 'Admin_login.html')

def Admin_dashboard(request):
    return render(request, 'dashboard.html')

def Registration(request):
    return render(request, 'Registration.html')



from django.shortcuts import render, redirect
from .forms import MeterReadingForm, EnergyVoucherForm
from .models import MeterReading, EnergyVoucher
#impor messages
from django.contrib import messages

def submit_reading(request):
    if request.method == 'POST':
        form = MeterReadingForm(request.POST)
        if form.is_valid():
            meter_reading = form.save(commit=False)
            meter_reading.customer = request.user
            meter_reading.save()
            return redirect('dashboard')
    else:
        form = MeterReadingForm()
    return render(request, 'submit_reading.html', {'form': form})

def redeem_voucher(request):
    if request.method == 'POST':
        form = EnergyVoucherForm(request.POST)
        if form.is_valid():
            voucher = EnergyVoucher.objects.get(code=form.cleaned_data['code'])
            if voucher.redeemed:
                messages.error(request, 'This voucher has already been redeemed.')
            else:
                voucher.redeemed = True
                voucher.customer = request.user
                voucher.save()
                request.user
