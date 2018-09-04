from rest_framework import serializers

import django
django.setup()

from .models import Advertisement, Accomodation_Review, Amenities, PropertyImage, Event
from .models import User_Profile, User_Review

class AdvertisementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('user', 'accommodation_name', 'accommodation_description',
                  'house_rules', 'booking_rules', 'base_price', 'num_guests',
                  'num_bedrooms', 'num_bathrooms', 'suburb', 'state', 'country')

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Profile
        field = ('user_name', 'name', 'email', 'profile_pic')

class UserReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = User_Review
        field = ('user', 'rating', 'title', 'message')

class Accomodation_ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Accomodation_Review
        field = ('advert', 'rating', 'title', 'message')

class AmentitiesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Amenities
        field = ('advert', 'feature')

# Not sure if this works, need to implement the encading thing 64byte
class PropertyImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = PropertyImage
        field = ('advert', 'image')

class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        field = ('advert', 'start_day', 'start_day_start_time', 'end_day',
                 'end_day_end_time', 'booking_status', 'notes')


''' code below is refactored to above code

class AdvertisementSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    # need to assign user to an instance of User_Profile
    user = serializers.IntegerField(required=True)
    accommodation_name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    accommodation_description = serializers.CharField(required=False, allow_blank=True, max_length=1000)

    house_rules = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    booking_rules = serializers.CharField(required=False, allow_blank=True, max_length=1000)

    base_price = serializers.IntegerField(required=True)

    num_guests = serializers.IntegerField(required=True)
    num_bedrooms = serializers.IntegerField(required=True)
    num_bathrooms = serializers.IntegerField(required=True)

    suburb = serializers.CharField(required=True, max_length=100)
    state = serializers.CharField(required=False, default='NSW', max_length=50)
    country = serializers.CharField(required=False, default='Australia', max_length=50)

    def create(self, validated_data):
        """
        Create and return a new 'Advertisement' instance, given the validated data.
        """
        return Advertisement.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing 'Advertisement' instance, given the validated_data.
        """

        instance.accommodation_name = validated_data.get('accommodation_name', instance.accommodation_name)
        instanceacc.accommodation_description = validated_data.get('accommodation_description', instance.accommodation_description)

        instance.house_rules = validated_data.get('house_rules', instance.house_rules)
        instance.booking_rules = validated_data.get('booking_rules', instance.booking_rules)

        instance.base_price = validated_data.get('base_price', instance.base_price)

        instance.num_guests = validated_data.get('num_guests', instance.num_guests)
        instance.num_bedrooms = validated_data.get('num_bedrooms', instance.num_bedrooms)
        instance.num_bathrooms = validated_data.get('num_bathrooms', instance.num_bathrooms)

        instance.suburb = validated_data.get('suburb', instance.suburb)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)

        return instance
'''

'''
To test in shell run the following commands:
python manage.py shell
from catalog.models import Advertisement
from catalog.serializers import AdvertisementSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import catalog.models as cat
u = cat.User_Profile.objects.all()
c = u[0]
a = Advertisement(accommodation_name='accom', accommodation_description='house', base_price=20.1, num_guests = 2, num_bedrooms = 3, num_bathrooms=1, suburb = 'hornsby', user = c)
a.save()
'''
