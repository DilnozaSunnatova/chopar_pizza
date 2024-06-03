from django.shortcuts import render

from rest_framework.generics import ListAPIView, ListCreateAPIView

from rest_framework import generics
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
import random
from datetime import timedelta,datetime
from . models import Product


from .serializers import AcsiyaSerializers, ContactSerializers, LocationSerializers

from .models import AcsiyaModel, ContactModel, LocationModel

from django.shortcuts import render, redirect



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
    

class AcsiyaListAPIView(ListAPIView):
    serializer_class = AcsiyaSerializers
    queryset = AcsiyaModel.objects.all()


class ContactListAPIView(ListCreateAPIView):
    def create_contact(request):
        if request.method == 'POST':
            form = ContactModel(request.POST)
            if form.is_valid():
                form.save()
                return redirect('success')
        else:
            form = ContactModel()
        return render(request, 'create_contact.html', {'form': form})
    
    serializer_class = ContactSerializers
    queryset = ContactModel.objects.all()
    
    

class LocationListAPIView(ListAPIView):
    serializer_class = LocationSerializers
    queryset = LocationModel.objects.all()
    
    




class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemListCreateView(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

class CartItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

@api_view(['POST'])
def add_quantity(request, pk):
    try:
        cart_item.quantity += 1
        cart_item = CartItem.objects.get(pk=pk)
        cart_item.save()
        return Response(CartItemSerializer(cart_item).data)
    except CartItem.DoesNotExist:
        return Response(status=404)

