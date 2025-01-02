from django.urls import path
from user_enquiry import views

urlpatterns=[
   path('',views.userclick,name='userclick'),
   path('loginreg/',views.userreg,name='ureg'),
   path('usertask/',views.usertask,name='usertask'),
   path('loginlog/',views.userlog,name='ulog'),
   path('ulogin/',views.ulogin,name='ulogin'),
   path('eqfm/',views.eqfm,name='eqfm'),
   path('eqtask/',views.eqtask,name='eqtask'),
   path('showpage/',views.ShowPage,name='showpage'),
   path('Delete/<int:id>/',views.delete,name='deletedata'),
   path('updaterec/<int:id>',views.updaterec,name='updaterec'),
 ]
