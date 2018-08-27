from django.contrib import admin

from .models import Advertisement, Accomodation_Review, Amenities, PropertyImage, Event
from .models import User_Profile, User_Review


class AmenitiesInline(admin.TabularInline):
    model = Amenities
    extra = 3


class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 3


class EventInline(admin.TabularInline):
    model = Event
    extra = 3
    #list_display = ['day', 'start_time', 'end_time', 'notes']


class UserReviewInline(admin.TabularInline):
    model = User_Review
    extra = 3

class AccommodationReviewInline(admin.TabularInline):
    model = Accomodation_Review
    extra = 3

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user_name']}),
        (None, {'fields': ['name']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['profile_pic']})
    ]
    inlines = [UserReviewInline]


class AdvertisementAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Owner', {'fields': ['user']}),
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
    inlines = [AmenitiesInline, PropertyImageInline, EventInline, AccommodationReviewInline]


admin.site.register(Advertisement, AdvertisementAdmin)
admin.site.register(User_Profile, UserAdmin)
