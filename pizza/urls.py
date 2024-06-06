from django.urls import path
from .views import DiscountAPIView,AboutAPIView,AuthenticationAPIView,UserLoginAPIView,InformationAPIView

urlpatterns=[
    path('discount/',DiscountAPIView.as_view()),
    path('about/',AboutAPIView.as_view()),
    path('register/', AuthenticationAPIView.as_view()),
    path('login/',UserLoginAPIView.as_view()),
    path('information/',InformationAPIView.as_view())
    
    
]