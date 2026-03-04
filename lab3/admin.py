from django.contrib import admin
from .models import Laptop, People, Delivery

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')

@admin.register(People)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'email', 'created_at', 'updated_at')

@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
    list_display = ('people', 'laptop', 'quantity', 'created_at', 'updated_at')