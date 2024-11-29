"""
Imports the Django database models module, which provides the base classes and functionality for defining database models in a Django application.
"""
from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    stars = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey('Business', on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    ordinal = models.IntegerField()
    business = models.ManyToManyField('Business')

class Business(models.Model): 
    LOW = '$'
    MID = '$$'
    HIGH = '$$$'
    
    PRICE_CHOICES = [
        (LOW, 'Very cheap'),
        (MID, 'Moderate'),
        (HIGH, 'Expensive')
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price_range = models.CharField(max_length=10, choices=PRICE_CHOICES, default=MID)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=50)
    url = models.URLField(max_length=255)
    phone = models.CharField(max_length=50)
    hours = models.CharField(max_length=255)