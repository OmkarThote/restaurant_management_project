from django.shortcuts import render
from django.conf import settings
# Create your views here.

def home(request):
    context = {
        'restaurant_name': 'Delicious_Bites',
        'welcome_message': 'welcome to Delicious Bites! Enjoy our tasty menu.',
        'phone_number':
    settings.RESTAURANT_PHONE_NUMBER
    }
return render(request, 'home.html', context)

def menu_items_view(ewquest):
    menu_items = [
        {"name": "Pizza", "Price": 8.99},
        {"name": "Burger", "Price": 5.49},
        {"name": "Pasta", "Price": 7.25},
        {"name": "Salad", "Price": 4.75},
    ]
    return render(request, "menu_items.html",
    {"menu_items": menu_items})
    