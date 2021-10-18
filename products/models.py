from django.db import models

"""Product Model"""
class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    price = models.FloatField
    stock = models.IntegerField
    
    def __str__(self):
        return self.name