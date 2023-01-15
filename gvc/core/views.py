#import render 
from django.shortcuts import render, redirect
# login required decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MeterReadingForm, EnergyVoucherForm
from .models import MeterReading, EnergyVoucher, Bill
#impor messages
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    reading_form = MeterReadingForm()
    voucher_form = EnergyVoucherForm()
    bills = Bill.objects.filter(customer=request.user).order_by('-bill_date')

    context = {
        'reading_form': reading_form,
        'voucher_form': voucher_form,
        'bills': bills,
    }
    return render(request, 'index.html', context)

def Admin_login(request):
    return render(request, 'Admin_login.html')

@login_required
def Admin_dashboard(request):
    return render(request, 'dashboard.html')

def Registration(request):
    return render(request, 'Registration.html')

def submit_reading(request):
    if request.method == 'POST':
        form = MeterReadingForm(request.POST)
        if form.is_valid():
            meter_reading = form.save(commit=False)
            meter_reading.customer = request.user
            meter_reading.save()
            return redirect('core:index')
    else:
        return redirect('core:index')

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
