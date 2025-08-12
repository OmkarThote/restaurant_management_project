from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', views.menu_items_view, name='menu_items'),
    
]