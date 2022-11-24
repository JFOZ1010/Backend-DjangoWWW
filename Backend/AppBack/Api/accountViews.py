from rest_framework import generics
from AppBack.Api.serializers import (
    AccountSerializer, 
    AccountAuthSerializer
)
from AppBack.models import Account
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
import http.client
import json, os
from dotenv import load_dotenv


class AccountCreateApi(generics.CreateAPIView):
    serializer_class = AccountSerializer
    model = Account
    permission_classes = [permissions.AllowAny]

class AccountUpdateApi(generics.UpdateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

class AccountRetrieveApi(generics.RetrieveAPIView):
    serializer_class = AccountSerializer
    model = Account
    permission_classes = [permissions.AllowAny]
    queryset = Account.objects.all()

class AccountAuthRetrieveApi(APIView):
    serializer_class = AccountAuthSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        
        userId = request.data['user_id']
        #userId = userId.replace("_", "|")
        """
        load_dotenv()

        print("Inicio de obtención token")
        conn = http.client.HTTPSConnection(os.getenv("AUTH0_DOMAIN"))
        #payload = "{\"client_id\":\"pgZrcTdU8hxWEhRfPITXZh7XUS7ROg6h\",\"client_secret\":\"OIBuojA8YR0lty2IY5b2okeGKSFXocW65SxfIv1XUP4--oI145EGvgmWwwEdC8AC\",\"audience\":\"https://dev-5fl4mhiern6wjoou.us.auth0.com/api/v2/\",\"grant_type\":\"client_credentials\"}"
        payload = "{\"client_id\":\""+ os.getenv('AUTH0_CLIENT_ID')+"\",\"client_secret\":\""+ os.getenv('CLIENT_SECRET')+"\",\"audience\":\"https://"+ os.getenv('AUTH0_DOMAIN')+"/api/v2/\",\"grant_type\":\"client_credentials\"}"

        headers = { 'content-type': "application/json" }

        conn.request("POST", "/oauth/token", payload, headers)

        res = conn.getresponse()
        data = res.read()
        datajson = json.loads(data.decode("utf-8"))
        token = datajson['access_token']
        
        bear = "Bearer " + token

        headers = { 'authorization' : bear}

        print("Inicio de obtencion usuario de auth")
        conn.request("GET", "/api/v2/users/" + userId , headers=headers)
        res = conn.getresponse()
        data = res.read()
        user_data = json.loads(data.decode("utf-8"))
        """
        print("Inicio de busqueda en bd")


        #userId = userId.replace("|", "_")
        #print(userId)
        cuenta = Account.objects.filter(user_id = userId).first()
        
        if (not(cuenta is None)):
            cuenta_dict = cuenta.__dict__
            if (cuenta_dict['user_type'] == 1):
                user_type = "Admin"
            elif (cuenta_dict['user_type'] == 2):
                user_type = "Supplier"
            else:
                user_type = "Cliente"
            
            user_status = cuenta_dict['user_status']
        else:
            user_type = 'noregistro'
            user_status = True
        
        #userId = userId.replace("_", "|")
        return Response({'authdata': 'por ahora no se puede', 'user_id': userId, 'user_type' : user_type, 'user_status' : user_status, 'token': 'no hay token'})