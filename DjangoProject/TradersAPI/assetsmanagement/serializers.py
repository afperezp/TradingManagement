from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import AssetsManagementClients

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer




class AssetsManagementClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsManagementClients
        fields = '__all__'
