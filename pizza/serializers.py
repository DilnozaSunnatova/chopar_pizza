from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .models import *



class AuthenticationSerializer(Serializer):

#     # phone = serializers.CharField()
#     # password = serializers.CharField()

    class Meta:
        model = Authentication
        fields =  '__all__'


class ProductDetailSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Product
        fields = "__all__"


class ExtraProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductExtra
        fields = "__all__"

