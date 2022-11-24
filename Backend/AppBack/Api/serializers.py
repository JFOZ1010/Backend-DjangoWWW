from rest_framework import serializers
from AppBack.models import User, Account, Supplier

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user_id', 'user_type', 'password', 'email', 'user_status']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_type', 'name', 'city', 'birth_date', 'sex']

class UserSerializerWithoutPk(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type', 'name', 'city', 'birth_date', 'sex']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['user_id', 'supplier_name']

class SupplierSerializerWithoutPk(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['supplier_name']

## Retreived Detailed serializers

class RetreiveUserAccountSerializer(serializers.ModelSerializer):
    user_id = AccountSerializer()

    class Meta: 
        model = User
        fields = ['user_id', 'user_type', 'name', 'city', 'birth_date', 'sex']


class RetreiveSupAccountSerializer(serializers.ModelSerializer):
    user_id = AccountSerializer()

    class Meta: 
        model = Supplier
        fields = ['user_id', 'supplier_name']

## Update Admin only: Special for deactive and active

class ActivationAdminSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields = ['user_id', 'user_status']