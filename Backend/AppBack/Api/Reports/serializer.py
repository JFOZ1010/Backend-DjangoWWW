from django.db.models import fields
from rest_framework import serializers
from AppBack.models import History
from AppBack.models import History_item
class HistorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = History
        fields = ['history_id','item_date','item_price']

class HistoryItemSerializer(serializers.ModelSerializer):
    history_id = HistorySerializer()
    class Meta: 
        model = History_item
        fields = ['history_id']

