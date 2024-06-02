from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import random
from datetime import timedelta,datetime
from rest_framework import generics
from . models import Product




class AuthenticationRegister(ListAPIView):
    serializer_class = AuthenticationSerializer
    queryset = Authentication.objects.all()



# class AuthenticationRegister(APIView):
#     def post(self,request,*args,**kwargs):
#         serializer = AuthenticationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         phone = serializer.data.get('phone')
#         password = serializer.data.get('password')

#         if Authentication.objects.filter(phone=phone,status='approved').exists():
#             raise serializers.ValidationError(
#                 detail={"error": "Bunday foydalanuvchi ro'yhatdan o'tgan"},
#                 code= 400
#             )
        
        

#         user = Authentication.objects.filter(phone=phone)
#         if user.exists():
#             user = user.first()
#         else:
#             user = Authentication.objects.create(phone=phone)


#         user.set_password(password)

         


#         code = random.randrange(1000, 9999)
#         user.code = code
#         user.expire_data = datetime.now() + timedelta(seconds=50)
#         user.save()
#         print(code)
#         return Response(
#             data = {
#                 "user": user.id
#             },
#             status = 201 
#         )
    
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class ExtraProductAPIView(generics.RetrieveAPIView):
    queryset = ProductExtra.objects.all()
    serializer_class = ExtraProductSerializer
