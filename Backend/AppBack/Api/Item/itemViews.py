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
from ...ScrappingFiles.scriptsScrappingArmando.script import ( amazonArmando, mercadolibreArmando, neweggArmando )
from ...ScrappingFiles.ScrappingGiron.scrapAmazon import scrapAmazonGiron
from ...ScrappingFiles.ScrappingGiron.scrapMercadoLibre import scrapMLGiron
from ...ScrappingFiles.ScrappingGiron.scrapNewegg import scrapNeweggGiron


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
        print(serialized.errors)
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
            print("**Scrapping amazon Kevin**")
            amazonKevin()
            print("**Scrapping amazon Julián**")
            #doAmazonGPU()
            #doAmazonRAM()
            print("**Scrapping amazon Giron**")
            scrapAmazonGiron()
            print("**Scrapping amazon Felipe**")
            #amazonJFOZ()
            print("**Scrapping amazon Armando**")
            amazonArmando()

        except Exception as e:
            print(str(e))
            return Response({ 'res' : 400, 'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({ 'res' : 200}, status = status.HTTP_200_OK)
        
class ScrappingMercadolibre(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            print("**Scrapping mercadolibre Kevin**")
            mercadolibreKevin()
            print("**Scrapping mercadolibre Julián**")
            #doMercadoLibreGPU()
            #doMercadoLibreRAM()
            print("**Scrapping mercadolibre Giron**")
            scrapMLGiron()
            print("**Scrapping mercadolibre Felipe**")
            #mercadolibreJFOZ()
            print("**Scrapping mercadolibre Armando**")
            mercadolibreArmando()


        except Exception as e:
            print(str(e))
            return Response({ 'res' : 400, 'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({ 'res' : 200}, status = status.HTTP_200_OK)

class ScrappingNewegg(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            print("**Scrapping newegg Kevin**")
            neweggKevin()
            print("**Scrapping newegg Julián**")
            #doNewEggGPU()
            #doNewEggRAM()
            print("**Scrapping newegg Giron**")
            scrapNeweggGiron()
            print("**Scrapping newegg Felipe**")
            #walmartJFOZ()
            print("**Scrapping newegg Armando**")
            neweggArmando()
            
        except Exception as e:
            print(str(e))
            return Response({ 'res' : 400, 'error': str(e)}, status = status.HTTP_400_BAD_REQUEST)
        else: 
            return Response({ 'res' : 200}, status = status.HTTP_200_OK)


