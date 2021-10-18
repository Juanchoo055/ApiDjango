from django.db import models

"""Clients model"""

class client(models.Model):
    document = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)