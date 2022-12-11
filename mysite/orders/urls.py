from .views import OrderViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('orders', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]