from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers
from .models import *



class AuthenticationSerializer(Serializer):
    class Meta:
        model = Authentication
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
    products = ProductDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Menu
        fields = "__all__"


