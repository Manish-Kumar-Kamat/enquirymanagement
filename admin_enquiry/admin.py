from django.contrib import admin
from .models import admindatabase
class serviceadmin(admin.ModelAdmin):
  list_display=('fname','phone','email','password')
admin.site.register(admindatabase,serviceadmin)
