from rest_framework import serializers
from AppBack.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['user_id', 'supplier_name']

class SupplierSerializerWithoutPk(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['supplier_name']