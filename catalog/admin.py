from django.contrib import admin

from .models import Advertisement, Accommodation_Review, PropertyImage
from .models import User_Profile, Event, PropertyRequest


class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['email']}),
        (None, {'fields': ['given_name']}),
        (None, {'fields': ['family_name']}),
        (None, {'fields': ['profile_pic']}),
        (None, {'fields': ['list_of_ads']}),
        (None, {'fields': ['list_of_rentals']}),
        (None, {'fields': ['list_of_posted_reviews']}),
    ]


class AdvertisementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Ad ID', {'fields': ['ad_id']}),
        ('Poster', {'fields': ['poster']}),
        ('Poster_ID', {'fields': ['poster_id']}),
        ('Accommodation Review IDs', {'fields': ['list_of_reviews']}),
        ('Event IDs', {'fields': ['list_of_events']}),
        ('Image IDs', {'fields': ['list_of_images']}),
        ('Accommodation Information',    {'fields': ['accommodation_name']}),
        (None, {'fields': ['accommodation_description']}),
        (None, {'fields': ['property_type']}),
        (None, {'fields': ['house_rules']}),
        (None, {'fields': ['booking_rules']}),
        (None, {'fields': ['amenities']}),
        (None, {'fields': ['base_price']}),
        (None, {'fields': ['num_guests']}),
        (None, {'fields': ['num_bedrooms']}),
        (None, {'fields': ['num_bathrooms']}),
        ('Location', {'fields': ['address']}),
        (None, {'fields': ['city']}),
        (None, {'fields': ['zip_code']}),
        (None, {'fields': ['latitude']}),
        (None, {'fields': ['longitude']}),
    ]


class AccommodationReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['rev_id']}),
        (None, {'fields': ['ad_owner']}),
        (None, {'fields': ['ad_id']}),
        (None, {'fields': ['reviewer']}),
        (None, {'fields': ['rating']}),
        (None, {'fields': ['message']}),
    ]


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['event_id']}),
        (None, {'fields': ['ad_owner']}),
        (None, {'fields': ['ad_id']}),
        (None, {'fields': ['booker']}),
        ('Rental Period', {'fields': ['start_day']}),
        (None, {'fields': ['start_day_start_time']}),
        (None, {'fields': ['end_day']}),
        (None, {'fields': ['end_day_end_time']}),
        ('booking_status', {'fields': ['booking_status']}),
        ('notes', {'fields': ['notes']}),
    ]


class PropertyImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['image_id']}),
        (None, {'fields': ['ad_owner']}),
        (None, {'fields': ['ad_id']}),
        (None, {'fields': ['pic']}),
    ]

class PropertyRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['text']}),
    ]


admin.site.register(User_Profile, UserAdmin)
admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Accommodation_Review, AccommodationReviewAdmin)
admin.site.register(PropertyImage, PropertyImageAdmin)
admin.site.register(PropertyRequest, PropertyRequestAdmin)
