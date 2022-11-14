from rest_framework import generics
from AppBack.Api.serializers import UserSerializer, AccountSerializer
from AppBack.models import User, Account
from rest_framework.response import Response
from rest_framework import status, viewsets, permissions

class UserCreateApi(generics.CreateAPIView):
    serializer_class = AccountSerializer
    model = Account
    #permission_classes = [permissions.AllowAny]