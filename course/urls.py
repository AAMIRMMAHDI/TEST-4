from django.urls import path
from .views import *

app_name = 'cours'

urlpatterns = [
    path('',course,name='course'),
    path('Trainers',trainers,name = 'Trainers')
]
