from django.db import models
from .orders import Orders
from .product import Product

class OrderProduct(models.Model):
    id_order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['id_order', 'id_product'], name='unique_order_product')
        ]

    def __str__(self):
        return f"{self.id_order} - {self.id_product}"
