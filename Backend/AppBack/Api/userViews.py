from rest_framework import generics
from AppBack.Api.serializers import (
    UserSerializer,  
    UserSerializerWithoutPk, 
)
from AppBack.models import Account, User
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

class UserCreateApi(generics.CreateAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        account = Account.objects.get(user_id = request.data['user_id'])
        serializer = self.serializer_class(data = request.data)
        
        if serializer.is_valid():
            serializer.save(user_id = account)
            return Response({'message': 'Se creo correctamente', 'data': serializer.data }, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class UserUpdateApi(generics.UpdateAPIView):
    serializer_class = UserSerializerWithoutPk
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()

class UserRetrieveApi(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    model = User
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()