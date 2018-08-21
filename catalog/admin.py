from django.contrib import admin

from .models import Advertisement, Amenities, PropertyImage, Event

# Register your models here.

class AmenitiesInline(admin.TabularInline):
    model = Amenities
    extra = 3


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3


class EventInline(admin.TabularInline):
    model = Event
    #list_display = ['day', 'start_time', 'end_time', 'notes']


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
    inlines = [AmenitiesInline, PropertyImageInline, EventInline]




admin.site.register(Advertisement, AdvertismentAdmin)
