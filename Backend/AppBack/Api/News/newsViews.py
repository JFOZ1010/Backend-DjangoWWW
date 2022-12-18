from django.shortcuts import render
from AppBack.models import New
from .serializer import NewSerializer
from django.shortcuts import get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from datetime import datetime, timedelta


from rest_framework import generics

from rest_framework import serializers

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status


# Create your views here.

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
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#CLASE PARA LISTAR
class allNew (generics.ListAPIView):
    serializer_class = NewSerializer
    model = New
    permission_classes = [permissions.AllowAny]
    queryset = New.objects.all()

    @receiver(request_started)
    def receiver_news(sender, **kwargs):
        for new in New.objects.all():
            dias = timedelta(days=30)

            if datetime.now().date() - new.new_date > dias:
                new.delete()
                print("se borro")
            else:
                print("no se borro")

    request_finished.connect(receiver)



#CLASE PARA OBTENER 1 ITEM
class NewGet(generics.RetrieveAPIView):
    serializer_class = NewSerializer
    model = New
    permission_classes = [permissions.AllowAny]
    queryset = New.objects.all()

#CLASE PARA BORRAR
class DeleteNew(generics.DestroyAPIView):
    serializer_class = NewSerializer
    model = New
    permission_classes = [permissions.AllowAny]
    queryset = New.objects.all()

    def delete(self, request, pk, format=None):
        new = self.get_object()
        new.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#CLASE PARA ACTUALIZAR 

class UpdateNew (generics.UpdateAPIView):
    serializer_class = NewSerializer
    model = New
    permission_classes = [permissions.AllowAny]
    queryset = New.objects.all()

    """
    def put(self, request, pk, format=None):
        new = self.get_object()
        serializer = self.serializer_class(new, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """

