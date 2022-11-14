from rest_framework import serializers
from AppBack.models import User, Account
from collections import OrderedDict

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_type', 'name', 'city', 'birth_date', 'sex']

class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = True)
    class Meta:
        model = Account
        fields = ['user_id', 'user_type', 'password', 'email', 'user']
        

    def create(self, validated_data):
        datos_usuario = validated_data.pop('user')
        del datos_usuario[0]['user_id']
        print(datos_usuario)
        account = Account.objects.create(**validated_data)
        for datos_usuario in datos_usuario:
            User.objects.create(user_id = account, **datos_usuario)
        return account

        