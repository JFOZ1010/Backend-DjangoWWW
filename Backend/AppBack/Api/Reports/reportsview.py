from .serializer import (
    HistorySerializer,
    HistoryItemSerializer
)
from AppBack.models import Item, History, History_item
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend


class AllHistoryItems(generics.ListAPIView):
    serializer_class = HistoryItemSerializer
    model = History_item
    permission_classes = [permissions.AllowAny]
    queryset = History_item.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item_id']
