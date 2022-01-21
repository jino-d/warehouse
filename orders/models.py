from django.contrib.auth.models import User
from django.db import models

from warehouses.models import Item


class Order(models.Model):
    """
    Ordered items made by User.
    """
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=20)
    ordered_by = models.ForeignKey(User)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_ordered']

    def __str__(self):
        return self.order_number


class OrderDetails(models.Model):
    """
    Status of ordered item.
    """
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    status_change_datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    address =  models.TextField(max_length=250)
    is_current = models.BooleanField(default=True)

    class Meta:
        ordering = ['date_ordered']

    def __str__(self):
        return u'{} - {}'.format(self.status_change_datetime, self.status)
