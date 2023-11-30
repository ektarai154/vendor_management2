# vendors/models.py
from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    # Add other fields as needed

class Product(models.Model):
    name = models.CharField(max_length=255)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    # Add other fields as needed
from django.db import models

# Create your models here.
