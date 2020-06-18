from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2, default=0.00, editable=False)

    class Meta:
        db_table = "pizza"
        managed = True


class Order(models.Model):
    user = models.ForeignKey(User, related_name="member", on_delete=models.CASCADE)
    order_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "order"
        managed = True


class OrderDetails(models.Model):
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    Qty = models.IntegerField(default=1)

    class Meta:
        managed = True
        db_table = "order_details"
