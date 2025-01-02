from django.contrib import admin
from .models import UserDataBase,UserEnquiry
class serviceadmin(admin.ModelAdmin):
  list_display=('fname','phone','email','password')
admin.site.register(UserDataBase,serviceadmin)

class serviceadmin(admin.ModelAdmin):
  list_display=('fname','email','phone','query')
admin.site.register(UserEnquiry,serviceadmin)

