from django.db import models

class RestaurantLocation(models.Model):
    name = models.CharField(max_length=100) # Restaurant name
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} - {self.city}, {self.state}"