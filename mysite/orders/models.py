from django.db import models
from users.models import CustomUser
from products.models import Product
import uuid


class Order(models.Model):
    buyer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="buyer")
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="seller")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, editable=False)
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    price = models.PositiveIntegerField(blank=True, null=True)
    quantity = models.PositiveIntegerField(blank=True, null=True)
    total = models.PositiveIntegerField(blank=True, null=True)
    size = models.CharField(blank=True, null=True, max_length=20)
    color = models.CharField(blank=True, null=True, max_length=30)
    fulfilled = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateTimeField(blank=True, null=True)
    estimated_delivery_date = models.DateField(null=True, blank=True, editable=True)



