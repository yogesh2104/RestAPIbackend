from dataclasses import fields
from rest_framework import serializers

from . models import UserData
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserData
        fields='__all__'