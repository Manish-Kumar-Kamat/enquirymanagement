from django.db import models

class admindatabase(models.Model):
	fname=models.CharField(max_length=30)
	phone=models.IntegerField()
	email=models.EmailField(max_length=40)
	password=models.CharField(max_length=40)