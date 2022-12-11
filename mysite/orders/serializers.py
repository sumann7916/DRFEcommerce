from rest_framework import serializers
from .models import Order
from products.models import Product

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        
    
    # def create(self, validated_data):
    #     order = Order.objects.create(**validated_data)
    #     product = Product.objects.filter(validated_data.pop)
    #     estimated_days = Product.objects.filter("")
    #     order.estimated_delivery_date = order.created