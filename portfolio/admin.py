from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from .models import Profile

@admin.register(Profile)
class ProifleAdmin(OSMGeoAdmin):
    list_display = (
     'home_address', 
     'phone_number',
     'location')