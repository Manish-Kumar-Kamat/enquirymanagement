
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('admindata/',include('admin_enquiry.urls')),
    path('logindata/',include('user_enquiry.urls')),
]
