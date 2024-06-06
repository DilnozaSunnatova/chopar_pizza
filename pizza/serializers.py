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
        exclude = ('product_size',)


class ProductDetailSerializer(serializers.ModelSerializer):
    product_sezee = serializers.ListSerializer(child=ProductSizeSerializer(), source='size')
    size = serializers.StringRelatedField(source='size.size')  
    menu = serializers.StringRelatedField(source='menu.name')
    class Meta:
        model = Product
        exclude = ('created_up','updated_up',)


class ExtraProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductExtra
        fields = "__all__"


class BranchSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField(source='region.name')
    class Meta:
        model = Branche
        fields = "__all__"


class ProductListSerializer(serializers.ModelSerializer):
    product_sizee = serializers.ListSerializer(child=ProductSizeSerializer(), source='size')
    size = serializers.StringRelatedField(source='size.size')  
    menu = serializers.StringRelatedField(source='menu.name')
    class Meta:
        model = Product
        exclude = ('created_up','updated_up',)


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = "__all__"


