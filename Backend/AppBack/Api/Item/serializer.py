from django.db.models import fields
from rest_framework import serializers
from AppBack.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Item
        fields = '__all__'

class ClicSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Item
        fields = ['item_clic']