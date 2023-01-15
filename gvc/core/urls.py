from django.urls import path
from .views import index, Admin_login, Admin_dashboard, Registration, submit_reading


app_name='core'


urlpatterns = [
    path('', index, name='index'),
    path('Admin_login/', Admin_login, name='Admin_login'),
    path('Admin_dashboard/', Admin_dashboard, name='Admin_dashboard'),
    path('Registration/', Registration, name='Registration'),
    path('submit_reading/', submit_reading, name='submit_reading'),
]
