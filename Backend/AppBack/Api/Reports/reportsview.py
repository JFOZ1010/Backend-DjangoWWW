
from AppBack.models import Item
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from ..Item.serializer import ItemSerializer


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

        