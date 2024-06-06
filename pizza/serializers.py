from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import About,Discount,User


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

   






    
        


















































