from django.contrib.auth import get_user_model
from django.db import models


class TimeStampedModel(models.Model):
    """
    An abstract class that serves as base class for other class.
    """

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(get_user_model)
    modified_by = models.ForeignKey(
        get_user_model, related_name="%(class)s_objects") 

    class Meta:
        abstract = True
