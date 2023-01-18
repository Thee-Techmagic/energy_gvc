
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from core.models import PropertyType, Customer
from .models import User
from django.urls import reverse

from .forms import LoginForm, CustomerForm,AdminForm
#importing staff_member_required
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('core:index'))
            else:
                
                return render(request, 'login.html', {'form': form, 'error': 'Invalid email or password'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#admin Login

def admin_view(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('Admin_panel:Admin_dash'))
            else:
                
                return render(request, 'admin_login.html', {'form': form, 'error': 'Invalid email or password'})
    else:
        form = AdminForm()
    return render(request, 'admin_login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        
        
        if form.is_valid():
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            return render(request, 'register.html', {'form': form, 'error': 'Invalid form'})
    else:
        form = CustomerForm()
    return render(request, 'register.html', {'form': form})

#create admin login