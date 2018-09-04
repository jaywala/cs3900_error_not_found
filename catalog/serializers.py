from rest_framework import serializers

<<<<<<< HEAD
from .models import Advertisement, Accomodation_Review, Amenities, PropertyImage, Event
from .models import User_Profile, User_Review

class AdvertisementSerializer(serializers.serializer):
=======
import django
django.setup()

from .models import Advertisement, Accomodation_Review, Amenities, PropertyImage, Event
from .models import User_Profile, User_Review

class AdvertisementSerializer(serializers.Serializer):
>>>>>>> jay

    id = serializers.IntegerField(read_only=True)
    # not sure if I need this as it's a ForeignKey
    # user = serializers.CharField(required=True, allow_blank=False, max_length=25)
    accommodation_name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    accommodation_description = serializers.CharField(required=False, allow_blank=True, max_length=1000)

    house_rules = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    booking_rules = serializers.CharField(required=False, allow_blank=True, max_length=1000)

    base_price = serializers.IntegerField(required=True, default=0)

    num_guests = serializers.IntegerField(required=True, allow_blank=False, default=0)
    num_bedrooms = serializers.IntegerField(required=True, allow_blank=False, default=0)
    num_bathrooms = serializers.IntegerField(required=True, allow_blank=False, default=0)

    suburb = serializers.CharField(required=True, allow_blank=False, max_length=100, default='')
    state = serializers.CharField(required=True, allow_blank=False, default='NSW', max_length=50)
    country = serializers.CharField(required=True, allow_blank=False, default='Australia', max_length=50)

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
