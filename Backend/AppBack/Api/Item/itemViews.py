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
            #print(serialized)
            #Se recorren todos los registros que se iban a insertar:
            for i in range(0, len(serialized.validated_data), 1):
                #Se verifica por cada registro si ya había uno en la base datos con exactamento el mismo nombre y proveedor
                if(len(Item.objects.filter(item_name=serialized.validated_data[i]['item_name'], user_id=serialized.validated_data[i]['user_id']))!=0):
                    print("Ya estaba")
                    #Si ya estaba, se verifica que las fechas sean diferentes 
                    if(Item.objects.get(item_name=serialized.validated_data[i]['item_name'], user_id=serialized.validated_data[i]['user_id']).item_date!=serialized.validated_data[i]['item_date']):
                        print("La fecha es diferente")
                        #Si las fechas son diferentes, se actualiza el registro que ya estaba
                        auxItem=Item.objects.get(item_name=serialized.validated_data[i]['item_name'])
                        auxItem.item_price=serialized.validated_data[i]['item_price']
                        auxItem.item_picture=serialized.validated_data[i]['item_picture']
                        auxItem.item_description='Se actualizó'
                        auxItem.item_url=serialized.validated_data[i]['item_url']
                        auxItem.item_date=serialized.validated_data[i]['item_date']
                        auxItem.type_id=serialized.validated_data[i]['type_id']
                        auxItem.save()
                        #Y se hace el guardado en el historial
                #En caso que no se encuentre un registro con el mismo nombre, simplemente se inserta a la base de datos
                else:
                    auxItem = Item(item_name=serialized.validated_data[i]['item_name'],
                                    item_price=serialized.validated_data[i]['item_price'],
                                    item_picture=serialized.validated_data[i]['item_picture'],
                                    item_description=serialized.validated_data[i]['item_description'],
                                    item_url=serialized.validated_data[i]['item_url'],
                                    item_date=serialized.validated_data[i]['item_date'],
                                    type_id=serialized.validated_data[i]['type_id'],
                                    user_id=serialized.validated_data[i]['user_id'])
                    auxItem.save()
            #print(len(serialized.validated_data))
            #print(serialized.validated_data[0])
            #serialized.save()
            #Y se da una respuesta exitosa
            return Response(serialized.data, status = status.HTTP_201_CREATED)
        #Si hubo algún error, se imprime y se da una respuesta 400
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


