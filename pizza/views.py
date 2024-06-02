from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .serializers import *




class UserRegister(ListAPIView):
    serializer_class = UserSerializer
    queryset = Authentication.objects.all()



