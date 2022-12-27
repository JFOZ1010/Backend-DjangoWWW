from rest_framework import generics
from .serializer import (
    ItemSerializer
)
from AppBack.models import Item
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView

class ItemCreateApi(generics.CreateAPIView):
    serializer_class = ItemSerializer
    model = Item
    permission_classes = [permissions.AllowAny]

class ItemCreateApi2(APIView):
    serializer_class = ItemSerializer
    model = Item
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serialized = self.serializer_class(data = request.data, many = True)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data, status = status.HTTP_201_CREATED)
        return Response(serialized._errors, status = status.HTTP_400_BAD_REQUEST)

class AllItems(generics.ListAPIView):
    serializer_class = ItemSerializer
    model = Item
    permission_classes = [permissions.AllowAny]
    queryset = Item.objects.all()