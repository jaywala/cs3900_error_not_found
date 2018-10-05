from rest_framework import serializers

import django
django.setup()

from .models import Advertisement, Accommodation_Review
from .models import User_Profile, Event, PropertyImage


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Profile
        field = ('user_name', 'name', 'email', 'profile_pic', 'list_of_ads',
                 'list_of_rentals', 'list_of_posted_reviews')
        exclude = ()


class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement

        fields = ('ad_id', 'poster', 'accommodation_name', 'accommodation_description',
                  'property_type', 'house_rules', 'booking_rules', 'amenities',
                  'base_price', 'num_guests', 'num_bedrooms', 'num_bathrooms',
                  'address', 'zip_code', 'latitude', 'longitude', 'list_of_reviews',
                  'list_of_events', 'list_of_images')
        exclude = ()


class AccommodationReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accommodation_Review
        field = ('rev_id', 'rating', 'message', 'ad_owner', 'ad_id')
        exclude = ()


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        field = ('event_id', 'ad_owner', 'ad_id', 'start_day', 'start_day_start_time'
                , 'end_day', 'end_day_end_time', 'booking_status', 'notes')
        exclude = ()


class PropertyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyImage
        field = ('image_id', 'ad_owner', 'ad_id', 'pic')
        exclude = ()
