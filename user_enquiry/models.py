from django.db import models

class UserDataBase(models.Model):
	fname=models.CharField(max_length=40)
	phone=models.IntegerField()
	email=models.EmailField(max_length=40)
	password=models.CharField(max_length=40)

class UserEnquiry(models.Model):
	fname=models.CharField(max_length=40)
	email=models.EmailField(max_length=40)
	phone=models.IntegerField()
	query=models.CharField(max_length=40)

