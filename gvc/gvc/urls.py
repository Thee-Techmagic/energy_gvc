from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('',include('core.urls',namespace='core')),
    path('api/',include('api.urls',namespace='api')),
    path('Admin_panel/',include('Admin_panel.urls',namespace='Admin_panel')),
]
