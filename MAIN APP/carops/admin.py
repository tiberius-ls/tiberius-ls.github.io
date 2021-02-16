from django.contrib import admin

# Register your models here.
from .models import Client, Car, MissingCar, Contact
admin.site.register(Client)
admin.site.register(Car)