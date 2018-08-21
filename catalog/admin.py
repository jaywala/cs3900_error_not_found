from django.contrib import admin

from .models import Advertisement, Amenities

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Amenities
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
    inlines = [ChoiceInline]





admin.site.register(Advertisement, AdvertismentAdmin)
