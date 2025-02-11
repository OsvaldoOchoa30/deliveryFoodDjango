from django.db import models
from .customer import Customer
from .delivery import Delivery

class Orders(models.Model):
    date = models.DateField(auto_now_add=True)  # Fecha automática al crear
    id_customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    id_delivery = models.ForeignKey(Delivery, on_delete=models.SET_NULL, null=True)  # Ajustado para permitir NULL

    def __str__(self):
        return f"Orden #{self.id}"