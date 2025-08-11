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