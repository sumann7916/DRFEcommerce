from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    
    description = models.TextField()
    category = models.ManyToManyField(Category)
    price = models.PositiveIntegerField(null=True, blank=True)
    ratings = models.PositiveIntegerField(null=True, blank=True)
    display_image = models.ImageField(null=True, blank=True)
    estimated_delivery_days = models.PositiveIntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.name




#Saving multiple images for product using separate table for images forming one to manu relationship
class Image(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product.name

