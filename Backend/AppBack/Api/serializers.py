from rest_framework import serializers
from AppBack.models import User, Account, Supplier

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_type', 'name', 'city', 'birth_date', 'sex']

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['user_id', 'supplier_name']
        
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type', 'name', 'city', 'birth_date', 'sex']

class SupplierUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['supplier_name']

class AccountUserSerializer(serializers.ModelSerializer):
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

class AccountSupplierSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(many = True)
    class Meta:
        model = Account
        fields = ['user_id', 'user_type', 'password', 'email', 'supplier']
        
    def create(self, validated_data):
        datos_supplier = validated_data.pop('supplier')
        del datos_supplier[0]['user_id']
        print(datos_supplier)
        account = Account.objects.create(**validated_data)
        for datos_supplier in datos_supplier:
            Supplier.objects.create(user_id = account, **datos_supplier)
        return account


class AccountUserUpdateSerializer(serializers.ModelSerializer):
    user = UserUpdateSerializer(many = True)
    class Meta:
        model = Account
        fields = ['user_type', 'password', 'email', 'user']

    def update(self, instance, validated_data):
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        datos_usuario = validated_data.pop('user')[0]
        datos_usuario = dict(datos_usuario)
        user = User.objects.get(user_id=instance.user_id)
        user.user_type = datos_usuario['user_type']
        user.name = datos_usuario['name']
        user.city = datos_usuario['city']
        user.birth_date = datos_usuario['birth_date']
        user.sex =  datos_usuario['sex']
        user.save()
        return instance

class AccountSupplierUpdateSerializer(serializers.ModelSerializer):
    supplier = SupplierUpdateSerializer(many = True)
    class Meta:
        model = Account
        fields = ['user_type', 'password', 'email', 'supplier']

    def update(self, instance, validated_data):
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        datos_supplier = validated_data.pop('supplier')[0]
        datos_supplier = dict(datos_supplier)
        supplier = Supplier.objects.get(user_id=instance.user_id)
        supplier.supplier_name = datos_supplier['supplier_name']
        supplier.save()
        return instance


        