from rest_framework import serializers

import django
django.setup()

from .models import Advertisement, Accommodation_Review
from .models import User_Profile, Event

class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement

        fields = ('ad_id', 'poster', 'accommodation_name', 'accommodation_description',
                  'house_rules', 'booking_rules', 'amenities', 'base_price', 'num_guests',
                  'num_bedrooms', 'num_bathrooms', 'suburb', 'state', 'country',
                  'latitude', 'longitude')

        exclude = ()

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Profile
        field = ('user_name', 'name', 'email', 'profile_pic', 'list_of_ads')
        exclude = ()


class AccommodationReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accommodation_Review
        field = ('accommodation_name','advert', 'rating', 'title', 'message')
        exclude = ()


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        field = ('accommodation_name', 'advert', 'start_day', 'start_day_start_time', 'end_day',
                 'end_day_end_time', 'booking_status', 'notes')
        exclude = ()
