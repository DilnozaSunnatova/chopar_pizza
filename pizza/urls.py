from django.urls import path
from .views import (AuthenticationAPIView, ProductDetailAPIView, ExtraProductAPIView, BrancheViewSet,
                    ProductListAPIView, ProductSizeListAPIView, ExtraProductListListAPIView, BranchsListApiview,
                    DiscountAPIView,AboutAPIView,AuthenticationAPIView,InformationAPIView,UserLoginAPIView,
                    MenuListAPIView)





from .views import DiscountAPIView,AboutAPIView,AuthenticationAPIView,UserLoginAPIView,InformationAPIView

urlpatterns=[

    # path('register/', AuthenticationRegister.as_view()),
    path('product-detail/<int:pk>', ProductDetailAPIView.as_view()),
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