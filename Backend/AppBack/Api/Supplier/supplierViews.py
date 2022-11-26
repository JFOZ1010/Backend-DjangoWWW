from rest_framework import generics
from .serializers import (
    SupplierSerializer, 
    SupplierSerializerWithoutPk
)
from AppBack.models import Account, Supplier
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

class SupplierCreateApi(generics.CreateAPIView):
    serializer_class = SupplierSerializer
    model = Supplier
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        account = Account.objects.get(user_id = request.data['user_id'])
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save(user_id = account)
            return Response({'message': 'Se creo correctamente', 'data': serializer.data }, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class SupplierUpdateApi(generics.UpdateAPIView):
    serializer_class = SupplierSerializerWithoutPk
    permission_classes = [permissions.AllowAny]
    queryset = Supplier.objects.all()

class SupplierRetrieveApi(generics.RetrieveAPIView):
    serializer_class = SupplierSerializer
    model = Supplier
    permission_classes = [permissions.AllowAny]
    queryset = Supplier.objects.all()

class RetreiveAllSuppliers(generics.ListAPIView):
    serializer_class = SupplierSerializer
    model = Supplier
    permission_classes = [permissions.AllowAny]
    queryset = Supplier.objects.all()