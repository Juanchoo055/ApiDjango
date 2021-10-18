from django.db import models
from django.db.models.fields.related import ForeignObject



# Create your models here.

    
# class bills(models.Model):
#     client_id = models.ForeignKey(client, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=50)
#     nit = models.CharField(max_length=50)
#     code = models.CharField(max_length=50)

#     def __str__(self):
#         return self.code


# class bills_products(models.Model):
#     bills_id = models.ForeignKey(bills, on_delete=models.CASCADE)
#     product_id = models.ForeignKey("products.products", on_delete=models.CASCADE)
#     quantity = models.IntegerField
#     price = m

