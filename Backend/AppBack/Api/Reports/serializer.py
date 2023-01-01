from django.db.models import fields
from rest_framework import serializers
from AppBack.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Item
        fields = ['item_id', 'item_name', 'item_picture', 'item_url', 'type_id', 'user_id', 'item_clic']