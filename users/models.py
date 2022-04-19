from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128, null=True, blank=True)
    last_name = models.CharField(max_length=128)
    username = models.CharField(max_length=250)
