from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('customer/login_customer/', views.login_view, name='login'),  
    path('staff/login_staff/', views.admin_view, name='login_staff'),
    path('customer/logout/', views.logout_view, name='customer_logout'),
    path('staff/logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    
]