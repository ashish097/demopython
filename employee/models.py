from django.db import models

# Create your models here.

class Employee(models.Model):
    id= models.CharField(max_length=10,blank=False,default='',primary_key=True)
    name= models.CharField(max_length=20,blank=False,default='')
    age= models.IntegerField(blank=False,default=3)
