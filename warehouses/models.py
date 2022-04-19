from django.db import models

from clients.models import Client
from core.models import TimeStampedModels


class Warehouse(TimeStampedModels):
    """
    A building/facility where the items are stored.
    """
    name = models.CharField(max_length=150)
    address = models.CharField()
    contact_number = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Item(TimeStampedModels):
    """
    A product that is distributed to the client.
    """
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=250)
    warehouse_id = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
