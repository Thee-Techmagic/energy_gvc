from core.models import PropertyType, Customer, EnergyVoucher, Payment
from .models import User
from django import forms
from django.contrib.auth import authenticate

class CustomerForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    repeat_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Repeat password', 'class': 'form-control'}))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    property_type = forms.ModelChoiceField(queryset=PropertyType.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    number_of_bedrooms = forms.IntegerField(widget=forms.NumberInput(attrs={'placeholder': 'Number of bedrooms', 'class': 'form-control'}))
    # voucher_code set to optional
    voucher_code = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': '8 Digit code', 'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        address = cleaned_data.get('address')
        property_type = cleaned_data.get('property_type')
        number_of_bedrooms = cleaned_data.get('number_of_bedrooms')
        voucher_code = cleaned_data.get('voucher_code') or None

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already exists')

        if password != cleaned_data.get('repeat_password'):
            raise forms.ValidationError('Passwords do not match')

        if not User.objects.filter(email=email).exists():
            user = User.objects.create_user(username=email, email=email, password=password)
            Customer.objects.create(user=user, address=address, property_type=property_type, number_of_bedrooms=number_of_bedrooms, voucher_code=voucher_code)

        try:
            if voucher_code:
                # if not EnergyVoucher.objects.filter(code=voucher_code).exists():
                #     raise forms.ValidationError('Invalid voucher code')
                # else:
                voucher = EnergyVoucher.objects.get(code=voucher_code)
                if voucher.redeemed:
                    raise forms.ValidationError('Voucher code already used')
                else:
                    voucher.redeemed = True
                    voucher.save()
        except:
             raise forms.ValidationError("Voucher code does not exist.")
         





class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError('Invalid email or password')


#create adminLoginForm
class AdminForm(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise forms.ValidationError('Invalid email or password')