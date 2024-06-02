from django.urls import path
from .views import AuthenticationRegister, ContactListAPIView

urlpatterns=[
    path('register/', AuthenticationRegister.as_view()),
    path('contact/', AuthenticationRegister.as_view()),
    
]