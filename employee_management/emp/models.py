from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Employee(models.Model):
    
    emp_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered Up to 10 digits allowed.")
    address = models.CharField(max_length=200,null=True)
    phone = models.CharField(validators=[phone_regex],max_length=10)
    
    department = models.CharField(max_length=200,null=True)
    working = models.BooleanField(default=True)
    
    
class Gallery(models.Model):
    
    uploadedby = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='uploads/')
    stars = models.CharField(max_length=5)