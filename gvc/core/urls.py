from django.urls import path
from .views import index,  submit_reading


app_name='core'


urlpatterns = [
    path('', index, name='index'),
    path('submit_reading/', submit_reading, name='submit_reading'),
    
    
]
