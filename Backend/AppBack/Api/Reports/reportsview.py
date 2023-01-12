from .serializer import (
    ItemSerializer,
    HistorySerializer,
    HistoryItemSerializer
)
from AppBack.models import Item
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from AppBack.models import Item, History, History_item
from ..Item.serializer import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ItemByCatApi(APIView):
    serializer_class = ItemSerializer
    model = Item
    permission_classes = [permissions.AllowAny]

    def get_queryset(self, type):
        return self.serializer_class.Meta.model.objects.filter(type_id = type).order_by('-item_clic')[:5]

    def post(self, request):
        rows = self.get_queryset(request.data['type_id'])

        if rows: 
            serialized_rows = self.serializer_class(rows, many= True)
            return Response(serialized_rows.data, status = status.HTTP_200_OK)
        else:
            return Response({'err': 'No se ha encontrado los datos'}, status = status.HTTP_404_NOT_FOUND)
   


##Gracias a Dios los serializers son los papás
class itemBySupplier(APIView):
    model = Item
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        ##Se filtran los objetos según el ID del proveedor, además se ordenan primero los más clickeados y finalmente se recorta para que muestre el top solicitado
        topItems = Item.objects.filter(user_id=request.data['user_id']).order_by('-item_clic')[:request.data['top']]
        if (len(topItems)!=0): 
            ##Toca serializarlo porque sino no se puede meter en la response
            serializated = ItemSerializer(topItems, many=True)
            ##Se retorna, en caso que se haya encontrado al menos un producto
            return Response(serializated.data, status = status.HTTP_200_OK) 
        else:
            ##Si no se encontró nada, igual toca responder lo obvio
            return Response("No hay items para mostrar", status = status.HTTP_404_NOT_FOUND)

class AllHistoryItems(generics.ListAPIView):
    serializer_class = HistoryItemSerializer
    model = History_item
    permission_classes = [permissions.AllowAny]
    queryset = History_item.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['item_id']
