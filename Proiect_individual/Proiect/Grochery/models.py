from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250,unique=True) 
    password = models.CharField(max_length=100)
