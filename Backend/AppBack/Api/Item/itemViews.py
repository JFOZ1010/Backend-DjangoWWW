from rest_framework import generics
from .serializer import (
    ItemSerializer
)
from AppBack.models import Item
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from ...ScrappingFiles.ScrappingKevin.amazon import amazon as amazonKevin
from ...ScrappingFiles.ScrappingKevin.newegg import newegg as neweggKevin
from ...ScrappingFiles.ScrappingKevin.mercadolibre import mercadolibre as mercadolibreKevin


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
        print(serialized._errors)
        return Response(serialized.errors, status = status.HTTP_400_BAD_REQUEST)

class AllItems(generics.ListAPIView):
    serializer_class = ItemSerializer
    model = Item
    permission_classes = [permissions.AllowAny]
    queryset = Item.objects.all()

class ScrappingAmazon(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            amazonKevin()

        except Exception as e:
            print(str(e))
            return Response({ 'res' : 400, 'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({ 'res' : 200}, status = status.HTTP_200_OK)

class ScrappingNewegg(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            neweggKevin()

        except Exception as e:
            print(str(e))
            return Response({ 'res' : 400, 'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({ 'res' : 200}, status = status.HTTP_200_OK)

class ScrappingMercadolibre(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            mercadolibreKevin()

        except Exception as e:
            print(str(e))
            return Response({ 'res' : 400, 'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({ 'res' : 200}, status = status.HTTP_200_OK)
