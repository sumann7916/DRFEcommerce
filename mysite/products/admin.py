from django.contrib import admin
from .models import Product, Category, Image

admin.site.register([Product, Category, Image])