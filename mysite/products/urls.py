from .views import ProductViewset, CategoryViewset, ImageViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('products',ProductViewset)
router.register('category',CategoryViewset)
router.register('images', ImageViewset)

urlpatterns = [
    path('api/', include(router.urls)),
]