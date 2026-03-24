from django.shortcuts import render
from .models import Laptop, People, Delivery

def home(request):
    items = Laptop.objects.all()
    return render(request, 'lab3/home.html', {'items': items})


def laptops(request):
    items = Laptop.objects.all()
    return render(request, 'lab3/laptops.html', {'items': items})