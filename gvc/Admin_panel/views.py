from django.shortcuts import render
from core.models import MeterReading
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def Admin_dash(request):
    meter=MeterReading.objects.all()
    
    #do the avarage of elecricity_day   
        

    #do the avarage of elecricity_night
    #do the avarage of gas
    context={
        'meter':meter
    }
    return render(request, 'admin.html',context)
