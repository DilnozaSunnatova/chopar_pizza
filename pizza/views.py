from django.shortcuts import render

from rest_framework.generics import ListAPIView

# Create your views here.

from .serializers import AcsiyaSerializers, ContactSerializers, LocationSerializers

from .models import AcsiyaModel, ContactModel, LocationModel


class AcsiyaListAPIView(ListAPIView):
    serializer_class = AcsiyaSerializers
    queryset = AcsiyaModel.objects.all()


class LocationListAPIView(ListAPIView):
    serializer_class = ContactSerializers
    queryset = ContactModel.objects.all()
    
    

class LocationListAPIView(ListAPIView):
    serializer_class = LocationSerializers
    queryset = LocationModel.objects.all()