from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.FloatField()
    category = models.CharField(max_length=50)
    images = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name