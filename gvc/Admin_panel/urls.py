from django.urls import  path
from .views import Admin_dash
app_name="Admin_panel"

urlpatterns = [
    path('', Admin_dash, name='Admin_dash'),
]