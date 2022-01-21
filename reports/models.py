from sre_parse import CATEGORIES
from django.contrib.auth.models import User
from django.db import models


class Report(models.Model):
    """
    Name and file path of generated reports.
    """

    name = models.CharField(max_length=20)
    directory = models.CharField(max_length=250)
    user_id = models.ForeignKey(User)
    category = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
