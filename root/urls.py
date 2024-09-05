from django.urls import path
from .views import home , contact , about
urlpatterns = [
    path('',home),
    path('contactus',contact) ,
    path('aboutus',about) ,
]
