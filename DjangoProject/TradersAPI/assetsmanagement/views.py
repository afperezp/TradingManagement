from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response

from .models import AssetsManagementClients
from .serializers import AssetsManagementClientSerializer

@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_movements_clients(request):
    all_movements = AssetsManagementClients.objects.all()
    assetsmovements_serializer = AssetsManagementClientSerializer(all_movements, many = True)
    return Response(assetsmovements_serializer.data)

