from django.urls import path
from .views import AuthenticationRegister

urlpatterns=[
    path('register/', AuthenticationRegister.as_view()),
    
    
]