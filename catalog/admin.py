from django.contrib import admin

from .models import Advertisement

# Register your models here.

class AdvertismentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Accommodation Information',    {'fields': ['accommodation_name']}),
        (None, {'fields': ['accommodation_description']}),
        ('Rules', {'fields': ['house_rules']}),
        (None, {'fields': ['booking_rules']}),
        ('Base Price', {'fields': ['base_price']}),
        ('Number of guests', {'fields': ['num_guests']}),
        ('Rooms', {'fields': ['num_bedrooms']}),
        (None, {'fields': ['num_bathrooms']}),
        ('Location', {'fields': ['suburb']}),
        (None, {'fields': ['state']}),
        (None, {'fields': ['country']}),
    ]





admin.site.register(Advertisement, AdvertismentAdmin)
