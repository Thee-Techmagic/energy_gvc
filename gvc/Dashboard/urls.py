from django.urls import path
from .views import index, Admin_login, Admin_dashboard, Registration


app_name='Dashboard'


urlpatterns = [
    path('', index, name='index'),
    path('Admin_login/', Admin_login, name='Admin_login'),
    path('Admin_dashboard/', Admin_dashboard, name='Admin_dashboard'),
    path('Registration/', Registration, name='Registration'),
]
