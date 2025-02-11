from django.db import models

class Delivery(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    status = models.BooleanField(default=True)  # Ahora tiene un valor por defecto
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} {self.last_name}"
