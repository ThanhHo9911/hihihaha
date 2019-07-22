from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=20)