from django.db import models

class Advertisement(models.Model):

    accommodation_name = models.CharField(max_length=50)
    accommodation_description = models.CharField(max_length=1000, default='')

    house_rules = models.CharField(max_length=1000, default='')
    booking_rules = models.CharField(max_length=1000, default='')

    base_price = models.IntegerField(default=0)

    num_guests = models.IntegerField(default=0)
    num_bedrooms = models.IntegerField(default=0)
    num_bathrooms = models.IntegerField(default=0)

    suburb = models.CharField(max_length=100, default='')
    state = models.CharField(default='NSW', max_length=50)
    country = models.CharField(default='Australia', max_length=50)

    def __str__(self):
        return self.accommodation_name

class Amenities(models.Model):
    # on_delete=models.CASCADE this means if the advertisement is deleted
    # the Amenities relying on the advertisement will also be deleted.
    advert = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    feature = models.CharField(max_length=200)

    def __str__(self):
        return self.feature
