from .models import *
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
import django_filters

from .models import AcsiyaModel, ContactModel, LocationModel, Product, CartItem

class AcsiyaSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = AcsiyaModel
        fields = "__all__"
        
class ContactSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = ContactModel
        fields = "__all__"
        
class LocationSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = LocationModel
        fields = "__all__"



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

#  Buni Abdulloh aka qilgan ekan men qo'shish uchun qilgandim o'chirsalariz bo'ladi

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Card Item bu hamma mahsulotlarni yig'ib beradi o'chirmanglar
class CartItemSerializer(serializers.ModelSerializer):
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = CartItem
        fields = '__all__'
