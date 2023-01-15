from django.db import models
from accounts.models import User
from django.utils.text import slugify
import datetime
# use decimal.Decimal for accurate calculations
import decimal

# Create your models here.

class PropertyType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PropertyType, self).save(*args, **kwargs)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'property types'
        db_table = 'property_type'

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    number_of_bedrooms = models.IntegerField()
    # 8 digit voucher code
    voucher_code = models.CharField(max_length=8, unique=True, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        # check voucher code validity
        if self.voucher_code:
            try:
                voucher = EnergyVoucher.objects.get(code=self.voucher_code)
                if voucher.redeemed:
                    raise ValueError('Voucher code has already been redeemed')
                else:
                    voucher.redeemed = True
                    voucher.save()
            except EnergyVoucher.DoesNotExist:
                raise ValueError('Voucher code is invalid')
        super(Customer, self).save(*args, **kwargs)

    class Meta:
        ordering = ['user']
        verbose_name_plural = 'customers'
        db_table = 'customer'


class MeterReading(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_date = models.DateField()
    electricity_day = models.DecimalField(max_digits=10, decimal_places=2,help_text='Electricity meter reading - Day (e.g. 100 kWh)')
    electricity_night = models.DecimalField(max_digits=10, decimal_places=2, help_text='Electricity meter reading - Night (e.g. 100 kWh)')
    gas = models.DecimalField(max_digits=10, decimal_places=2, help_text='Gas meter reading (e.g. 800 kWh)')

    def __str__(self):
        return self.customer.username

    class Meta:
        ordering = ['-submission_date']
        verbose_name_plural = 'meter readings'
        db_table = 'meter_reading'
        

    def save(self, *args, **kwargs):
        # calculate bill amount and save to bill table
        bill_amount = 0
        # get previous meter reading if it exists
        try:
            previous_reading = MeterReading.objects.filter(customer=self.customer).latest('submission_date')
            # calculate bill amount
            bill_amount += (self.electricity_day - previous_reading.electricity_day) * decimal.Decimal(0.15)
            bill_amount += (self.electricity_night - previous_reading.electricity_night) * decimal.Decimal(0.05)
            bill_amount += (self.gas - previous_reading.gas) * decimal.Decimal(0.05)
        except MeterReading.DoesNotExist:
            # first reading, no bill
            bill_amount = 0
        # save bill
        bill = Bill(customer=self.customer, amount=bill_amount, bill_date=self.submission_date)
        bill.save()
        super(MeterReading, self).save(*args, **kwargs)





class Bill(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    bill_date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.customer.username

    class Meta:
        ordering = ['-bill_date']
        verbose_name_plural = 'bills'
        db_table = 'bill'

class Payment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_date = models.DateField(default=datetime.date.today)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.customer.username

    class Meta:
        ordering = ['-payment_date']
        verbose_name_plural = 'payments'
        db_table = 'payment'

class EnergyVoucher(models.Model):
    code = models.CharField(max_length=8, unique=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    redeemed = models.BooleanField(default=False)


    def __str__(self):
        return self.code

    class Meta:
        ordering = ['code']
        verbose_name_plural = 'energy vouchers'
        db_table = 'energy_voucher'




