from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication 
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from django_filters.rest_framework import DjangoFilterBackend

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user_type']



