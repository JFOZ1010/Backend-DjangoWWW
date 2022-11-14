from rest_framework import generics
from AppBack.Api.serializers import AccountUserSerializer, AccountSupplierSerializer, AccountUserUpdateSerializer, AccountSupplierUpdateSerializer
from AppBack.models import Account
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

class AccountUserCreateApi(generics.CreateAPIView):
    serializer_class = AccountUserSerializer
    model = Account
    permission_classes = [permissions.AllowAny]

class AccountSupplierCreateApi(generics.CreateAPIView):
    serializer_class = AccountSupplierSerializer
    model = Account
    permission_classes = [permissions.AllowAny]


class AccountUserUpdateApi(generics.UpdateAPIView):
    serializer_class = AccountUserUpdateSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

class AccountSupplierUpdateApi(generics.UpdateAPIView):
    serializer_class = AccountSupplierUpdateSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()
    

class AccountUserRetreiveApi(generics.RetrieveAPIView):
    serializer_class = AccountUserSerializer
    model = Account
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

class AccountSupplierRetreiveApi(generics.RetrieveAPIView):
    serializer_class = AccountSupplierSerializer
    model = Account
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

