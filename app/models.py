from django.db import models

# Create your models here.
class Doctor(models.Model):
	phone = models.IntegerField()
	name = models.CharField(max_length=500)
	speciality = models.CharField(max_length=500)
	hospital = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now=True)


class User(models.Model):
	phone = models.IntegerField()
	name = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now=True)
	cardid = models.IntegerField()


class Report(models.Model):
	timestamp = models.DateTimeField(auto_now=True)
	doctor = models.ForeignKey('Doctor',on_delete=models.CASCADE)
	user = models.ForeignKey('User',on_delete=models.CASCADE)


class Attachment(models.Model):
	filename = models.CharField(max_length=500)
	report = models.ForeignKey('Report',on_delete=models.CASCADE)
