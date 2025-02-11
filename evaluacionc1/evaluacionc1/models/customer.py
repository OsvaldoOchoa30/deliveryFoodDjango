from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} {self.last_name}"