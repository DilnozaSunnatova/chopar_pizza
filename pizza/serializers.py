from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .models import *



class UserSerializer(serializers.Serializer):
    class Meta:
        model = Authentication
        fields =  '__all__'

