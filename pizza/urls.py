from django.urls import path
from .views import AuthenticationRegister, ContactListAPIView, ProductListCreateView, ProductDetailView, CartItemListCreateView, ProductDetailAPIView, ExtraProductAPIView, AdressCostumerListCreateView, CartItemDetailView, add_quantity

from .views import (AuthenticationAPIView, ProductDetailAPIView, ExtraProductAPIView, BrancheViewSet,
                    ProductListAPIView, ProductSizeListAPIView, ExtraProductListListAPIView, BranchsListApiview,
                    DiscountAPIView,AboutAPIView,AuthenticationAPIView,InformationAPIView,UserLoginAPIView,
                    MenuListAPIView)





from .views import DiscountAPIView,AboutAPIView,AuthenticationAPIView,UserLoginAPIView,InformationAPIView

urlpatterns=[

    # path('register/', AuthenticationRegister.as_view()),
    path('product-detail/<int:pk>', ProductDetailAPIView.as_view()),
    path('extra-product/<int:pk>', ExtraProductAPIView.as_view()),
    path('contact-register/', ContactListAPIView.as_view(),  name='contact-list-create'),
    path('adress-enter/', AdressCostumerListCreateView.as_view(),  name='contact-list-create'),
    path('api/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('api/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('api/cart-items/', CartItemListCreateView.as_view(), name='cartitem-list-create'),
    path('api/cart-items/<int:pk>/', CartItemDetailView.as_view(), name='cartitem-detail'),
    path('api/cart-items/<int:pk>/add_quantity/', add_quantity, name='add-quantity'),
    path('extra-product/<int:pk>', ExtraProductAPIView.as_view()),
    path('branch/<int:pk>', BrancheViewSet.as_view()),
    path('productlist/', ProductListAPIView.as_view()),
    path('productsize/', ProductSizeListAPIView.as_view()),
    path('extraprodlist/', ExtraProductListListAPIView.as_view()),
    path('branchlist/', BranchsListApiview.as_view()),
    path('menulist/', MenuListAPIView.as_view()),
    path('discount/',DiscountAPIView.as_view()),
    path('about/',AboutAPIView.as_view()),
    path('register/', AuthenticationAPIView.as_view()),
    path('login/',UserLoginAPIView.as_view()),
    path('information/',InformationAPIView.as_view()),
    
    
]