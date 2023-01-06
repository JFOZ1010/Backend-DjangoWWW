from rest_framework import serializers
from AppBack.models import Account, User, Supplier

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user_id', 'user_type', 'password', 'email', 'user_status']

class AccountAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user_id']

class ActivationAdminSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Account
        fields = ['user_id', 'user_status']


#NESTED SERIALIZERS
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