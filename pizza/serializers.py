from rest_framework.serializers import Serializer 
from rest_framework import serializers
from .models import *



class AuthenticationSerializer(Serializer):

#     # phone = serializers.CharField()
#     # password = serializers.CharField()

    class Meta:
        model = Authentication
        fields =  '__all__'



