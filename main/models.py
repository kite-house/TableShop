from django.db import models

# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.CharField(max_length=300)


