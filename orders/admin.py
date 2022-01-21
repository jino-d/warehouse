from django.contrib import admin

from .models import Order
from .models import OrderDetails


admin.site.register(Order)
admin.site.register(OrderDetails)
