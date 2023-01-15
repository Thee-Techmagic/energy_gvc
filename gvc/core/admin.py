from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(PropertyType)
admin.site.register(MeterReading)
admin.site.register(Bill)
admin.site.register(EnergyVoucher)

admin.site.site_header = "Energy GVC Admin"
admin.site.site_title = "Energy GVC Admin Portal"