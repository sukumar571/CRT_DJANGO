from django.db import models

# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=100)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    course=models.CharField(max_length=20)
    graduation=models.CharField(max_length=50)
    address=models.CharField(max_length=100)
    pincode=models.CharField(max_length=10)
    desig=models.CharField(max_length=20,)
