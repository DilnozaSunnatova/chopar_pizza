from .models import *
from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
import django_filters

from .models import AcsiyaModel, ContactModel, LocationModel, Product, CartItem, AdressCostumer

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

from .models import About,Discount,User
from . models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import About,Discount,User


class AuthenticationSerializer(Serializer):
    class Meta:
        model = User
        fields =  '__all__'


class ProductSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductSize
        fields = '__all__'



class ExtraProductSerializer(serializers.ModelSerializer):
    extra_products = serializers.StringRelatedField(source='extra_products.name') 
    class Meta:
        model = ProductExtra
        fields = "__all__"



class ProductDetailSerializer(serializers.ModelSerializer):
    product_sezee = serializers.ListSerializer(child=ProductSizeSerializer(), source='size')
    size = serializers.StringRelatedField(source='size.size')  
    menu = serializers.StringRelatedField(source='menu.name')
    
    class Meta:
        model = Product
        exclude = ('created_up','updated_up',)


class BranchSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField(source='region.name')
    class Meta:
        model = Branche
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    product_sizee = serializers.ListSerializer(child=ProductSizeSerializer(), source='size')
    size = serializers.StringRelatedField(source='size.size')  
    menu = serializers.StringRelatedField(source='menu.name')
    name = serializers.StringRelatedField(source='name.name') 
    class Meta:
        model = Product
        exclude = ('created_up','updated_up',)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
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

class AdressCostumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdressCostumer
        fields = '__all__'




class DiscountSerializer(ModelSerializer):

    class Meta:
        model = Discount
        fields = '__all__'


class AboutSeriliazer(ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'


class UserSerializer(serializers.Serializer):
    phone = serializers.CharField()
    password = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()
    name = serializers.CharField()

class LoginSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            'phone',
            'password',
        )


class InformationSerializer(serializers.Serializer):

    phone = serializers.CharField()
    email= serializers.EmailField()
    birth_date = serializers.DateField()
    name = serializers.CharField()

   






    
        


















































