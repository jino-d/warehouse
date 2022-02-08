from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField()
    contact_number = models.CharField(max_length=20)
    is_active = models.BooleanField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
