from myapp.models import Restaurant

Restaurant.objects.create(
    name="Food Plaza",
    address="123 MG Road, Bangalore",
    opening_hours={
        "Monday": "9 AM - 9 PM",
        "Tuesday": "9 AM - 9 PM",
        "Wednesday": "9 AM - 9 PM",
        "Thursday": "9 AM - 9 PM",
        "Friday": "9 AM - 9 PM",
        "Sunday": "Closed",
    }
)