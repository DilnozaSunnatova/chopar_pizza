from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import DiscountSerializer,AboutSeriliazer,UserSerializer,InformationSerializer,LoginSerializer
from .models import Discount,About,User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from datetime import datetime, timedelta
import random
from rest_framework.serializers import ValidationError

class DiscountAPIView(ListAPIView):
    serializer_class= DiscountSerializer
    queryset = Discount.objects.all()
  
class AboutAPIView(ListAPIView):
    serializer_class = AboutSeriliazer
    queryset = About.objects.all()


class AuthenticationAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data.get('phone')
        password = serializer.validated_data.get('password')
        birth_date = serializer.validated_data.get('birth_date')
        name = serializer.validated_data.get('name')
        gender = serializer.validated_data.get('gender')
        if User.objects.filter(phone=phone, status='approved').exists():
            raise ValidationError(
                detail={"error": "Bunday foydalanuvchi ro'yxatdan o'tgan"},
                code=400
            )
        
        user = User.objects.filter(phone=phone)
        if user.exists():
            user = user.first()
        else:
            user = User.objects.create(phone=phone, birth_date=birth_date, name=name,gender = gender)
        user.set_password(password)
        code = random.randrange(1000, 9999)      
        user.code = code
        user.expire_date = datetime.now() + timedelta(seconds=60)
        user.save()

        print(code)
        return Response(
            data={
                "user": user.id,

                "name": user.name,
                "phone": user.phone,
                "gender": user.gender,
                "birth_date": user.birth_date


            },
            status=201
            )
    

class InformationAPIView(APIView):
    def post(self,request, *args,**kwargs):
        serializer = InformationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        name = serializer.validated_data.get("name")
        phone = serializer.validated_data.get("phone")
        email = serializer.validated_data.get("email")
        birth_date = serializer.validated_data.get("birth_date")

        user = User.objects.create(name= name,phone=phone,email=email,birth_date=birth_date)
       

        return Response(
            data={
                
                'user': user.id,
                "name": user.name,
                "phone": user.phone,
                "email": user.email,
                "birth_date": user.birth_date

            }
        )
  
class UserLoginAPIView(APIView):
    
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)

        phone = request.data.get('phone')
        password = request.data.get('password')

        user = authenticate(phone=phone, password=password)

        if user is None or user.status != "approved":
            raise ValidationError(detail={
                "error":"Siz ro'yxatdan o'tmagansiz"},
                code = 400
                )


        token, created = Token.objects.get_or_create(user=user)
        return Response(
            data={
                'token': token.key,
                'user': user.id
            }
        )





































































































































































# from django.shortcuts import render
# from rest_framework.views import APIView,Response
# from . import serializers
# from rest_framework.generics import ListAPIView,RetrieveAPIView
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.filters import SearchFilter
# from . import models


# class InformationAPIView(CreateAPIView):
#     serializer_class = InformationSerializer
#     querset = Authentication.objects.all()







    



































# class AuthenticationRegister(ListAPIView):
#     serializer_class = AuthenticationSerializer
#     queryset = Authentication.objects.all()



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
    
