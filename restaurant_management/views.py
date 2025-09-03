from django.shortcuts import render
from .models import OpeningHours

def home(request):
    hours = OpeningHours.objects.all().order_by('id')