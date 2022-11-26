from django.db.models import fields
from rest_framework import serializers
from AppBack.models import New

class NewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = New
        #fields = ('new_id','new_title','new_image','new_description')
        fields = '__all__'