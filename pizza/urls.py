from django.urls import path
from .views import (AuthenticationRegister, ProductDetailAPIView, ExtraProductAPIView, BrancheViewSet,
                    ProductListSerializer, ProductSizeListAPIView, ExtraProductListListAPIView, BranchsListApiview)
from rest_framework.routers import DefaultRouter





urlpatterns=[
    path('register/', AuthenticationRegister.as_view()),
    path('product-detail/<int:pk>', ProductDetailAPIView.as_view()),
    path('extra-product/<int:pk>', ExtraProductAPIView.as_view()),
    path('branch/<int:pk>', BrancheViewSet.as_view()),
    path('productlist/', ProductListSerializer.as_view()),
    path('productsize/', ProductSizeListAPIView.as_view()),
    path('extraprodlist/', ExtraProductListListAPIView.as_view()),
    path('branchlist/', BranchsListApiview.as_view())
    
    
]