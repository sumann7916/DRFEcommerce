from rest_framework import serializers
from .models import CustomUser
from rest_framework.authtoken.views import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'address', 'city', 'company_name', 'user_type']

        extra_kwargs = {'password':{
            'write_only': True,
            'required': True,
        }}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

    def get_student(self, request):
        queryset = CustomUser.objects.filter(user_type=1)
        