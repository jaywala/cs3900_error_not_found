from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError


class User_Profile(models.Model):

    user_name = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50) # this is the unique identier
    profile_pic = models.CharField(null=True, blank=True, max_length=1000)

    # contains the ad id's that this user owns
    list_of_ads = models.CharField(null=True, blank=True, max_length=1000)

    def __str__(self):
        return self.email

    #--------------------------------

    def get_user_name(self):
        return self.user_name

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_profile_pic(self):
        return self.profile_pic

    def get_list_of_ads(self):
        return self.list_of_ads

    #--------------------------------

    def set_user_name(self, new_user_name):
        u = User_Profile.objects.get(id=self.id)
        u.user_name = new_user_name
        u.save()

    def set_name(self, new_name):
        u = User_Profile.objects.get(id=self.id)
        u.name = new_name
        u.save()

    def set_email(self, new_email):
        u = User_Profile.objects.get(id=self.id)
        u.email = new_email
        u.save()

    def set_profile_pic(self, new_pic):
        u = User_Profile.objects.get(id=self.id)
        u.profile_pic = new_pic
        u.save()

    def set_list_of_ads(self, new_list_of_ads):
        u = User_Profile.objects.get(id=self.id)
        u.list_of_ads = new_list_of_ads
        u.save()

    #--------------------------------

    def delete_me(self):
        self.delete()


class Advertisement(models.Model):

    ad_id = models.IntegerField() # this is the unique identier

    # contains the ad review id's that this ad owns
    list_of_reviews = models.CharField(null=True, blank=True, max_length=1000)

    #  contains the event id's that this ad owns
    list_of_events = models.CharField(null=True, blank=True, max_length=1000)

    poster = models.CharField(null=True, blank=True, max_length=1000)

    accommodation_name = models.CharField(null=True, blank=True, max_length=1000)
    accommodation_description = models.CharField(null=True, blank=True, max_length=1000)

    house_rules = models.CharField(null=True, blank=True, max_length=1000)
    booking_rules = models.CharField(null=True, blank=True, max_length=1000)

    amenities=models.CharField(null=True, blank=True, max_length=1000)

    base_price = models.FloatField(null=True, blank=True, max_length=1000)

    num_guests = models.IntegerField(null=True, blank=True)
    num_bedrooms = models.IntegerField(null=True, blank=True)
    num_bathrooms = models.IntegerField(null=True, blank=True)

    suburb = models.CharField(null=True, blank=True, max_length=1000)
    state = models.CharField(null=True, blank=True, max_length=1000)
    country = models.CharField(null=True, blank=True, max_length=1000)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        temp = str(self.ad_id) + ', ' + str(self.poster) + ', ' + str(self.accommodation_name)
        return temp

    #--------------------------------

    def get_ad_id(self):
        return self.ad_id

    def get_rev_ids(self):
        return self.list_of_reviews

    def get_event_ids(self):
        return self.list_of_events

    def get_poster(self):
        return self.poster

    def get_accommodation_name(self):
        return self.accommodation_name

    def get_accommodation_description(self):
        return self.accommodation_description

    def get_house_rules(self):
        return self.house_rules

    def get_booking_rules(self):
        return self.booking_rules

    def get_amenities(self):
        return self.amenities

    def get_base_price(self):
        return self.base_price

    def get_num_guests(self):
        return self.num_guests

    def get_num_bedrooms(self):
        return self.num_bedrooms

    def get_num_bathrooms(self):
        return self.num_bathrooms

    def get_suburb(self):
        return self.suburb

    def get_state(self):
        return self.state

    def get_country(self):
        return self.country

    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    #--------------------------------

    def set_ad_id(self, new_ad_id):
        a = Advertisement.objects.get(id=self.id)
        a.ad_id = new_ad_id
        a.save()

    def set_rev_ids(self, new_list_of_rev):
        a = Advertisement.objects.get(id=self.id)
        a.list_of_reviews = new_list_of_rev
        a.save()

    def set_event_ids(self, new_list_of_event):
        a = Advertisement.objects.get(id=self.id)
        a.list_of_events = new_list_of_event
        a.save()

    def set_poster(self, new_poster):
        a = Advertisement.objects.get(id=self.id)
        a.poster = new_poster
        a.save()

    def set_accommodation_name(self, new_accommodation_name):
        a = Advertisement.objects.get(id=self.id)
        a.accommodation_name = new_accommodation_name
        a.save()

    def set_accommodation_description(self, new_accommodation_description):
        a = Advertisement.objects.get(id=self.id)
        a.accommodation_description = new_accommodation_description
        a.save()

    def set_house_rules(self, new_house_rules):
        a = Advertisement.objects.get(id=self.id)
        a.house_rules = new_house_rules
        a.save()

    def set_booking_rules(self, new_booking_rules):
        a = Advertisement.objects.get(id=self.id)
        a.booking_rules = new_booking_rules
        a.save()

    def set_amenities(self, new_amenities):
        a = Advertisement.objects.get(id=self.id)
        a.amenities = new_amenities
        a.save()

    def set_base_price(self, new_base_price):
        a = Advertisement.objects.get(id=self.id)
        a.base_price = new_base_price
        a.save()

    def set_num_guests(self, new_num_guests):
        a = Advertisement.objects.get(id=self.id)
        a.num_guests = new_num_guests
        a.save()

    def set_num_bedrooms(self, new_num_bedrooms):
        a = Advertisement.objects.get(id=self.id)
        a.num_bedrooms = new_num_bedrooms
        a.save()

    def set_num_bathrooms(self, new_num_bathrooms):
        a = Advertisement.objects.get(id=self.id)
        a.num_bathrooms = new_num_bathrooms
        a.save()

    def set_suburb(self, new_suburb):
        a = Advertisement.objects.get(id=self.id)
        a.suburb = new_suburb
        a.save()

    def set_state(self, new_state):
        a = Advertisement.objects.get(id=self.id)
        a.state = new_state
        a.save()

    def set_country(self, new_country):
        a = Advertisement.objects.get(id=self.id)
        a.country = new_country
        a.save()

    def set_latitude(self, new_latitude):
        a = Advertisement.objects.get(id=self.id)
        a.latitude = new_latitude
        a.save()

    def set_longitude(self, new_longitude):
        a = Advertisement.objects.get(id=self.id)
        a.longitude= new_longitude
        a.save()

    #--------------------------------

    def delete_me(self):
        self.delete()


class Accommodation_Review(models.Model):

    rev_id = models.IntegerField() # this is the unique identier

    rating = models.IntegerField()
    message = models.CharField(max_length=1000)

    ad_owner = models.CharField(max_length=100)
    ad_id =  models.IntegerField()

    def __str__(self):
        return str(self.rev_id) + ", " + self.ad_owner

    #--------------------------------

    def get_rev_id(self):
        return self.rev_id

    def get_rating(self):
        return self.rating

    def get_message(self):
        return self.message

    def get_ad_owner(self):
        return self.ad_owner

    def get_ad_id(self):
        return self.ad_id

    #--------------------------------

    def set_rev_id(self, new_id):
        u = Accommodation_Review.objects.get(id=self.id)
        u.rev_id = new_id
        u.save()

    def set_rating(self, new_rating):
        u = Accommodation_Review.objects.get(id=self.id)
        u.rating = new_rating
        u.save()

    def set_message(self, new_message):
        u = Accommodation_Review.objects.get(id=self.id)
        u.message = new_message
        u.save()

    def set_ad_owner(self, new_ad_owner):
        u = Accommodation_Review.objects.get(id=self.id)
        u.ad_owner = new_ad_owner
        u.save()

    def set_ad_id(self, new_ad_id):
        u = Accommodation_Review.objects.get(id=self.id)
        u.ad_id = new_ad_id
        u.save()

    #--------------------------------

    def delete_me(self):
        self.delete()


class Event(models.Model):

    event_id = models.IntegerField()
    ad_owner = models.CharField(max_length=100)
    ad_id =  models.IntegerField()

    start_day = models.DateField(u'Start day of the rent', help_text=u'Start day of the rent')
    start_day_start_time = models.TimeField(u'Starting time', help_text=u'Starting time')

    end_day = models.DateField(u'End day of the event', help_text=u'End day of the event')
    end_day_end_time = models.TimeField(u'End time', help_text=u'End time')

    booking_status = 'booked'

    notes = models.TextField(u'Notes', help_text=u'Notes', blank=True, null=True)

    def __str__(self):
        temp = str(self.event_id) + ', ' + str(self.start_day)
        return temp

    #--------------------------------

    class Meta:
        verbose_name = u'Event'
        verbose_name_plural = u'Events'

    def check_overlap(self, fixed_start_day, fixed_start_day_start_time, fixed_end_day, fixed_end_day_end_time,
                      new_start_day, new_start_day_start_time, new_end_day, new_end_day_end_time, event):

        overlap = False
        if self.advert.pk == event.advert.pk:
            if fixed_start_day == new_end_day or fixed_end_day == new_start_day:
                if fixed_start_day_start_time <= new_end_day_end_time or fixed_end_day_end_time >= new_end_day_end_time:
                    overlap = True
            elif fixed_start_day == new_start_day or fixed_end_day == new_end_day:
                overlap = True
            elif (fixed_start_day >= new_start_day and fixed_end_day <= new_end_day) or (fixed_start_day <= new_start_day and fixed_end_day >= new_end_day):
                overlap = True
            elif (fixed_start_day >= new_start_day and fixed_end_day <= new_start_day) or (fixed_start_day <= new_start_day and fixed_end_day >= new_start_day):
                overlap = True

        return overlap

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_day))

    def clean(self):
        if self.start_day > self.end_day:
            raise ValidationError('Ending day, ' + str(self.end_day) + ', must be after starting day ' + str(self.start_day))
        if self.start_day == self.end_day and self.start_day_start_time >= self.end_day_end_time:
            raise ValidationError('Ending time, ' + str(self.end_day_end_time) + ', must be after starting time ' + str(self.start_day_start_time
            ) + ', since it\'s on the same day')

        events = Event.objects.all()
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_day, event.start_day_start_time, event.end_day, event.end_day_end_time,
                                      self.start_day, self.start_day_start_time, self.end_day, self.end_day_end_time
                                      , event) and event.id != self.id:
                    raise ValidationError(
                         'There is an overlap with another event: ' + 'the new event --> self ' + str(self.notes
                         ) + ' ' + str(self.booking_status) + ', ' + 'old event --> event ' + str(event.notes
                         ) + ' ' + str(event.booking_status))
                        #'There is an overlap with another event: ' + str(event.start_day) + ', ' + str(
                        #    event.start_day_start_time) + '-' + str(event.end_day) + ', ' + str(event.end_day_end_time))

    def check_validity(self):
        if self.start_day > self.end_day:
            return False
        if self.start_day == self.end_day and self.start_day_start_time >= self.end_day_end_time:
            return False

        events = Event.objects.all()
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_day, event.start_day_start_time, event.end_day, event.end_day_end_time,
                                      self.start_day, self.start_day_start_time, self.end_day, self.end_day_end_time
                                      ) and event.id != self.id:
                    return False
        return True

    #--------------------------------

    def get_event_id(self):
        return self.event_id

    def get_start_day(self):
        return self.start_day

    def get_start_day_start_time(self):
        return self.start_day_start_time

    def get_end_day(self):
        return self.end_day

    def get_end_day_end_time(self):
        return self.end_day_end_time

    def get_booking_status(self):
        return self.booking_status

    def get_notes(self):
        return self.notes

    def get_ad_owner(self):
        return self.ad_owner

    def get_ad_id(self):
        return self.ad_id

    #--------------------------------

    def set_event_id(self, new_id):
        u = Event.objects.get(id=self.id)
        u.event_id = new_id
        u.save()

#TODO need to check the validity when using these methods to modify the data
# currently it trivaly either modifies db or doesn't.
# need to return some feed back to user.
# above case is valid when creating the event. Just not for editing the event.
    def set_start_day(self, new_start_day):
        e = Event.objects.get(id=self.id)
        if e.check_validity() == True: # this is not working the way I want
            e.start_day = new_start_day
            e.save()

    def set_start_day_start_time(self, new_start_time):
        e = Event.objects.get(id=self.id)
        e.start_day_start_time = new_start_time
        e.save()

    def set_end_day(self, new_end_day):
        e = Event.objects.get(id=self.id)
        e.end_day = new_end_day
        e.save()

    def set_end_day_end_time(self, new_end_time):
        e = Event.objects.get(id=self.id)
        e.end_day_end_time = new_end_time
        e.save()

    def set_booking_status(self, new_booking_status):
        e = Event.objects.get(id=self.id)
        e.booking_status = new_booking_status
        e.save()

    def set_notes(self, new_notes):
        e = Event.objects.get(id=self.id)
        e.notes = new_notes
        e.save()

    def set_ad_owner(self, new_ad_owner):
        u = Event.objects.get(id=self.id)
        u.ad_owner = new_ad_owner
        u.save()

    def set_ad_id(self, new_ad_id):
        u = Event.objects.get(id=self.id)
        u.ad_id = new_ad_id
        u.save()

    #--------------------------------

    def delete_me(self):
        self.delete()


class PropertyImage(models.Model):

    image_id = models.IntegerField()
    ad_owner = models.CharField(max_length=100)
    ad_id = models.IntegerField()

    pic = models.CharField(max_length=500000)

    def __str__(self):
        return str(self.image_id) + ", " + self.ad_owner
