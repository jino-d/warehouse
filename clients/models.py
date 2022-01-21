from django.db import models

from core.models import TimeStampedModel


class Client(TimeStampedModel):
    """
    The one who receives items distributed from warehouse.
    """
    name = models.CharField(max_length=250)
    address = models.CharField()
    contact_number = models.CharField(max_length=20)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
