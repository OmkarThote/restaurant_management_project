from django.urls import path
from .views import *
from . import views

urlpatterns = [
    
]


urlpatterns = [
    path('', views.home, name='home'),
]


