from django.contrib.auth import get_user_model
from django.db import models


class Report(models.Model):
    """
    Name and file path of generated reports.
    """

    name = models.CharField(max_length=20)
    directory = models.FileField()
    user = models.ForeignKey(get_user_model, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
