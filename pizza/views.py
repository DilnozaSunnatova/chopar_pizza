from django.shortcuts import render

from rest_framework.generics import ListAPIView

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import random
from datetime import timedelta,datetime




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