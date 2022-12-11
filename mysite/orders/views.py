from django.shortcuts import render
from .serializers import OrderSerializer
from .models import Order
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['buyer', 'seller', 'product_id', 'is_paid', 'estimated_delivery_date']
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)



