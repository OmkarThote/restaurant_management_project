# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_menu(request):
    menu = [
        {
            "name": "Margherita Pizza",
            "description": "Classic pizza with tomato sauce, mozzarella, and cheese", 
            "price": 8.99
        },
        {
            "name": "Veggie Burger",
            "description": "Grilled veggie patty with lettuce, tomato, and cheese",
            "price": 7.49
        },
        {
            "name": "Pasta Alfredo",
            "description": "Pasta in creamy Alfredo sauce with mushrooms",
            "price": 10.50
        }
    ]
    return Response(menu)


    