from django.db.models import fields
from rest_framework import serializers
from AppBack.models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Item
        #fields = ('new_id','new_title','new_image','new_description')
        fields = '__all__'