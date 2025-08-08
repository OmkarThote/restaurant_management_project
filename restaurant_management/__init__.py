# models.py

from django.db import models

class Restaurant(models.Models):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name