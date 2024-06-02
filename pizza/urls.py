from django.urls import path
from .views import AuthenticationRegister, ProductDetailAPIView, ExtraProductAPIView

urlpatterns=[
    path('register/', AuthenticationRegister.as_view()),
    path('product-detail/<int:pk>', ProductDetailAPIView.as_view()),
    path('extra-product/<int:pk>', ExtraProductAPIView.as_view())
    
    
]