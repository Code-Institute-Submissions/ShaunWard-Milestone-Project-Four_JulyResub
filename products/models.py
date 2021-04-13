from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    dimensions = models.CharField(max_length=70, null=True, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.name