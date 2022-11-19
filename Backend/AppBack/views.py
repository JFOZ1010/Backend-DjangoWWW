from django.shortcuts import render
from .models import New
from .serializers import NewSerializer
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
#importar la vista de new


# Create your views here.

"""INICIA BLOQUE DE CRUD DE NOTICIA"""
@api_view(['GET'])
def NewOverview(request):
    new_urls = {
        'all_items': 'all/',
        'Add': 'create/',
        'Update': 'update/pk/',
        'Delete': 'delete/pk/'
    }

  
    return Response(new_urls)

#FUNCION CREAR
@api_view(['POST','GET'])
def addNews(request):
    new = NewSerializer(data=request.data)
  
    # validating for already existing data
    if New.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if new.is_valid():
        new.save()
        return Response(new.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

"""FIN BLOQUE DE CRUD DE NOTICIA"""

#funcion para obtener todos los datos
@api_view(['GET'])
def allNews(pk=None):
    news = New.objects.all()
    serializer = NewSerializer(news, many=True)
    return Response(serializer.data)


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
    return Response(status=status.HTTP_202_ACCEPTED)
