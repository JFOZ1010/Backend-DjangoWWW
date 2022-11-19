from django.shortcuts import render
from .models import New
from .serializers import NewSerializer

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
        'all_items': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/New/pk/delete'
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
def allNews(request):
    new = New.objects.all()
    new_serializer = NewSerializer(new, many=True)
    return Response(new_serializer.data)


#funcion para actualizar un dato
@api_view(['POST'])
def updateNew(request, pk):
    new = New.objects.get(id=pk)
    new_serializer = NewSerializer(instance=new, data=request.data)
    if new_serializer.is_valid():
        new_serializer.save()
    return Response(new_serializer.data)

#funcion para eliminar un dato
@api_view(['DELETE'])
def deleteNew(pk, request):
    new = New.objects.get(id=pk)
    new.delete()
    return Response('New successfully deleted!')
