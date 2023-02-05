from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status



from .serializers import MyTokenObtainPairSerializer
from .models import Clients, Trader
from .serializers import UserSerializer, TraderSerializer, ClientSerializer,RegisterSerializer,ChangePasswordSerializer, UpdateUserSerializer


"""
Token JWT Auth
"""

class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer

User = get_user_model()

"""
Users Management

"""
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer



class UpdateProfileView(generics.UpdateAPIView):

    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateUserSerializer


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)





@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_users(request):
    users = User.objects.all()
    user_serializer = UserSerializer(users, many = True)
    return Response(user_serializer.data)



@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def get_user(request, pk):
    if request.method =="GET":
        user = User.objects.filter(id = pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)
    elif request.method =="POST":
        return Response("Request no valida. Por favor indica el ENDPOINT: /")


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def create_user(request):
    if request.method =="POST":
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            print("is valid!")
            user_serializer.create(user_serializer.data)
            user_serializer.save()
            return Response("Se ha creado correctamente el user.")
        return Response(user_serializer.errors)
    elif request.method =="GET":
        return Response("Es una peticion get")


    
#TODO
@api_view(["POST", "GET", "UPDATE"])
@permission_classes([IsAuthenticated])
def update_user(request, pk):
    if request.method =="POST":
        user_serializer = UserSerializer(request.data)
        if user_serializer.is_valid():
            user = Trader.objects.create(user_serializer.data)
            user.save()
            return Response("Se ha creado correctamente el user.")
        return Response(user_serializer.errors)
    
#TODO
@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_user(request, pk):
    if request.method =="POST":
        user_serializer = UserSerializer(request.data)
        user = User.objects.filter(id = pk).first()
        if user_serializer.is_valid():
            user = Trader.objects.create(user_serializer.data)
            user.save()
            return Response("Se ha creado correctamente el user.")
        return Response(user_serializer.errors)

"""

#TODO
"""
"""
Traders Management

@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_traders(request):
    traders = Trader.objects.all()
    traders_serializer = TraderSerializer(traders, many = True)
    return Response(traders_serializer.data)


#TODO
@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def get_trader_detail(request, pk):
    if request.method =="GET":
        trader = Trader.objects.filter(id = pk).first()
        trader_serializer = TraderSerializer(trader)
        return Response(trader_serializer.data)


#TODO
@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def create_trader(request, pk):
    if request.method =="POST":
        trader_serializer = TraderSerializer(request.data)
        if trader_serializer.is_valid():
            trader = Trader.objects.create(trader_serializer.data)
            trader.save()
            return Response("Se ha creado correctamente el trader.")
        return Response(trader_serializer.errors)

        

#TODO
"""

"""
Clients Management
@api_view(["GET"])
@permission_classes([AllowAny])
def get_all_clients(request):
    users = User.objects.all()
    user_serializer = ClientSerializer(users, many = True)
    return Response(user_serializer.data)


@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def get_client_details(request, pk):
    if request.method =="GET":
        user = User.objects.filter(id = pk).first()
        user_serializer = ClientSerializer(user)
        return Response(user_serializer.data)

@api_view(["POST", "GET"])
@permission_classes([IsAuthenticated])
def create_client(request, pk):
    if request.method =="GET":
        user = User.objects.filter(id = pk).first()
        user_serializer = ClientSerializer(user)
        return Response(user_serializer.data)
        


        """