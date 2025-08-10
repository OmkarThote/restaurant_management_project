from django.shortcuts import render

# Create your views here.

from .models import Restaurant

def home(request):
    restaurant = Restaurant.objects.first()

# get first Restaurant

return render(request, 'home.html',
{
    'restaurant_name': restaurant.name if restaurant else 'No Name'
})

def home(request):
    return render(request, 'home_html')



def custom_404(request, exception):
    return render(request, '404.html', status=404)