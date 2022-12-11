from .models import Product, Image, Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'ratings']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['product', 'image']

    
