from rest_framework import generics
from .serializer import (
    ItemSerializer
)
from AppBack.models import Item
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

class ItemCreateApi(generics.CreateAPIView):
    serializer_class = ItemSerializer
    model = Item
    permission_classes = [permissions.AllowAny]
