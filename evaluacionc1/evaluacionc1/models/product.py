from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()  
    price = models.IntegerField()
    amount = models.IntegerField()
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
