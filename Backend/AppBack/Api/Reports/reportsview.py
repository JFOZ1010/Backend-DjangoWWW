from .serializer import (
    ItemSerializer,
)
from AppBack.models import Item
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics


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