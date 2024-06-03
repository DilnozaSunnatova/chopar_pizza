from django.urls import path
from .views import AuthenticationRegister, ContactListAPIView, ProductListCreateView, ProductDetailView, CartItemListCreateView, ProductDetailAPIView, ExtraProductAPIView, CartItemDetailView, add_quantity


urlpatterns=[
    path('register/', AuthenticationRegister.as_view()),
    path('product-detail/<int:pk>', ProductDetailAPIView.as_view()),
    path('extra-product/<int:pk>', ExtraProductAPIView.as_view()),
    path('contact/', ContactListAPIView.as_view(),  name='contact-list-create'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/cart-items/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('api/cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cartitem-detail'),
    path('api/cart-items/<int:pk>/add_quantity/', add_quantity, name='add-quantity'),
]