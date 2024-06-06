from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import random
from datetime import timedelta,datetime
from rest_framework import generics, viewsets
from . models import Product
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter



class AuthenticationRegister(ListAPIView):
    serializer_class = AuthenticationSerializer
    queryset = Authentication.objects.all()

    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ExtraProductAPIView(generics.RetrieveAPIView):
    queryset = ProductExtra.objects.all()
    serializer_class = ExtraProductSerializer


class BrancheViewSet(generics.RetrieveAPIView):
    queryset = Branche.objects.all()
    serializer_class = BranchSerializer


class ProductSizeListAPIView(ListAPIView):
    queryset = ProductSize.objects.all()
    serializer_class = ProductSizeSerializer

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends =[DjangoFilterBackend,]
    filterset_fields = ("name",)
    search_fields = ('menu',)


class ExtraProductListListAPIView(ListAPIView):
    queryset = ProductExtra.objects.all()
    serializer_class = ExtraProductSerializer


class BranchsListApiview(ListAPIView):
    queryset = Branche.objects.all()
    serializer_class = BranchSerializer


class MenuListAPIView(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    filter_backends =[DjangoFilterBackend,]
    filterset_fields = ("name",)
    
    
