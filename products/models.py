from django.db import models
from django.db.models.deletion import CASCADE
from django.http.response import HttpResponse

# Create your models herec
class products(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField(max_length=20, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    products = models.ForeignKey(products, on_delete=models.CASCADE)
    date_of_created = models.DateField(max_length=100, null=True)
    def __str__(self):
        return self.products.name