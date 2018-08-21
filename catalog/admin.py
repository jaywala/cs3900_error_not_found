from django.contrib import admin

from .models import Advertisement, Amenities, PropertyImage

# Register your models here.

class AmenitiesInline(admin.TabularInline):
    model = Amenities
    extra = 3

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3

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
    inlines = [AmenitiesInline, PropertyImageInline]




admin.site.register(Advertisement, AdvertismentAdmin)
