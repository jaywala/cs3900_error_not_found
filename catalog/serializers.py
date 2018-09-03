from rest_framework import serializers

from .models import Advertisement, Accomodation_Review, Amenities, PropertyImage, Event
from .models import User_Profile, User_Review

class AdvertisementSerializer(serializers.serializer):

    id = serializers.IntegerField(read_only=True)
    # not sure if I need this as it's a ForeignKey
    # user = serializers.CharField(required=True, allow_blank=False, max_length=25)
    accommodation_name = serializers.CharField(required=True, allow_blank=False, max_length=50)
    accommodation_description = serializers.CharField(required=False, allow_blank=True, max_length=1000)

    house_rules = serializers.CharField(required=False, allow_blank=True, max_length=1000)
    booking_rules = serializers.CharField(required=False, allow_blank=True, max_length=1000)

    base_price = serializers.IntegerField(required=True, allow_blank=False, default=0)

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
        '''
        instance. = validated_data.get()
        instance. = validated_data.get()
        instance. = validated_data.get()

        instance. = validated_data.get()
        instance. = validated_data.get()
        instance. = validated_data.get()

        instance. = validated_data.get()
        instance. = validated_data.get()
        instance. = validated_data.get()

        instance. = validated_data.get()
        instance. = validated_data.get()
        instance. = validated_data.get()
        '''
