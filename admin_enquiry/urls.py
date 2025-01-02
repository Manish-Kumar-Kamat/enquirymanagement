from django.urls import path
from admin_enquiry import views

urlpatterns=[
   path('',views.adminclick,name='adminclick'),
   path('adminreg/',views.adminreg,name='areg'),
   path('adminlog/',views.adminlog,name='alog'),
   path('regtask/',views.regtask,name='insertdata'),
   path('alog/',views.alogin,name='alogin'),  
]

