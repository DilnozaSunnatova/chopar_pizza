from rest_framework import serializers
import django_filters

from .models import AcsiyaModel, ContactModel, LocationModel

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
        
from rest_framework.serializers import Serializer 
from rest_framework import serializers
from .models import *



class AuthenticationSerializer(Serializer):

#     # phone = serializers.CharField()
#     # password = serializers.CharField()

    class Meta:
        model = Authentication
        fields =  '__all__'



