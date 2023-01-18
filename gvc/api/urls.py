from django.urls import path
from .views import property_type_list

app_name = 'api'

urlpatterns=[
    path('', property_type_list, name='api'),
]