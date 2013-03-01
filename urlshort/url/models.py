from django.db import models

class Data(models.Model):
	actualurl = models.CharField(max_length=200)
	tinyurl = models.CharField(max_length=200)
	randomcode = models.CharField(max_length=200)
# Create your models here.
