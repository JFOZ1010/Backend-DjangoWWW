from django.shortcuts import render
from AppBack.models import New
from .serializer import NewSerializer
from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError

from rest_framework import generics

from rest_framework import serializers

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status


# Create your views here.

"""INICIA BLOQUE DE CRUD DE NOTICIA"""
"""@api_view(['GET'])
def NewOverview(request):
    new_urls = {
        'all_items': 'all/',
        'Add': 'create/',
        'Update': 'update/pk/',
        'Delete': 'delete/pk/'
    }

  
    return Response(new_urls)"""

#CLASE CREAR
class addNews (generics.CreateAPIView):
    serializer_class = NewSerializer
    model = New
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


#CLASE PARA LISTAR
class allNew (generics.ListAPIView):
    serializer_class = NewSerializer
    model = New
    permission_classes = [permissions.AllowAny]
    queryset = New.objects.all()



#crear una clase para eliminar una New, y returne un http 204
    
class DeleteNew(generics.DestroyAPIView):
    serializer_class = NewSerializer
    model = New
    permission_classes = [permissions.AllowAny]
    queryset = New.objects.all()

    def delete(self, request, pk, format=None):
        new = self.get_object()
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""FIN BLOQUE DE CRUD DE NOTICIA
    #funcion para actualizar un dato
    @api_view(['POST'])
    def updateNew(request, pk):
        new = New.objects.get(pk=pk)
        data = NewSerializer(instance=new, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


    #funcion para eliminar un dato
    @api_view(['DELETE'])
    def deleteNew(request, pk):
        #new = New.objects.get(pk=pk)
        new = get_object_or_404(New, pk=pk)
        new.delete()
        return Response(status=status.HTTP_202_ACCEPTED)"""
