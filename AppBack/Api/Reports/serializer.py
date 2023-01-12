from django.db.models import fields
from rest_framework import serializers
from AppBack.models import History, History_item, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Item
        fields = ['item_id', 'item_name', 'item_picture', 'item_url', 'type_id', 'user_id', 'item_clic']

class HistorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = History
        fields = ['history_id','item_date','item_price']

class HistoryItemSerializer(serializers.ModelSerializer):
    history_id = HistorySerializer()
    class Meta: 
        model = History_item
        fields = ['history_id']

