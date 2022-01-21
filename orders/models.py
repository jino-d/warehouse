from django.contrib.auth import get_user_model
from django.db import models

from core.models import TimeStampedModel
from warehouses.models import Item


class Order(TimeStampedModel):
    """
    Ordered items made by User.
    """
    item = models.ForeignKey(Item)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=20)
    ordered_by = models.ForeignKey(get_user_model, on_delete=models.CASCADE)


    class Meta:
        ordering = ['date_ordered']

    def __str__(self):
        return self.order_number


class OrderDetails(models.Model):
    """
    Status of ordered item.
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status_change_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    address =  models.TextField(max_length=250)
    is_current = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_ordered']

    def __str__(self):
        return f'{self.status_change_datetime} - {self.status}'
