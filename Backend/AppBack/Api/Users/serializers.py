from rest_framework import serializers
from AppBack.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_type', 'name', 'city', 'birth_date', 'sex']

class UserSerializerWithoutPk(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type', 'name', 'city', 'birth_date', 'sex']