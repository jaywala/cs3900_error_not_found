from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

class User_Profile(models.Model):

    user_name = models.CharField(max_length=25)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to = 'profile_pics/')

    def __str__(self):
        return self.user_name

    def get_user_name(self):
        return self.user_name

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    #--------------------------------

    def set_name(self, new_name):
        u = User_Profile.objects.get(id=self.id)
        u.name = new_name
        u.save()

    def set_email(self, new_email):
        u = User_Profile.objects.get(id=self.id)
        u.email = new_email
        u.save()

    #--------------------------------
    '''
    def create_me(self, user_name, name, email, profile_pic):
        u = User_Profile(user_name=user_name, name=name, email=email, profile_pic=profile_pic)
        u.save()
    '''
    #--------------------------------

    def delete_me(self):
        self.delete()

    #--------------------------------

    def exists(username):
        '''
        Searches for the object by a field.
        '''
        user = User_Profile.objects.filter(user_name=username)
        if user.exists() and len(user) == 1:
            return user
        else:
            return None





class User_Review(models.Model):

    user = models.ForeignKey(User_Profile, related_name='user_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def get_user(self):
        return self.user

    def get_rating(self):
        return self.rating

    def get_title(self):
        return self.title

    def get_message(self):
        return self.message

    #--------------------------------

    def set_rating(self, new_rating):
        u = User_Review.objects.get(id=self.id)
        u.rating = new_rating
        u.save()

    def set_title(self, new_title):
        u = User_Review.objects.get(id=self.id)
        u.title = new_title
        u.save()

    def set_message(self, new_message):
        u = User_Review.objects.get(id=self.id)
        u.message = new_message
        u.save()

    #--------------------------------
    '''
    def create_me():
        u = User_Review()
    '''
    #--------------------------------

    def delete_me(self):
        self.delete()


class Advertisement(models.Model):

    user = models.ForeignKey(User_Profile, related_name='advertisements', on_delete=models.CASCADE)
    accommodation_name = models.CharField(max_length=50)
    accommodation_description = models.CharField(max_length=1000, default='')

    house_rules = models.CharField(max_length=1000, default='')
    booking_rules = models.CharField(max_length=1000, default='')

    base_price = models.IntegerField(default=0)

    num_guests = models.IntegerField(default=0)
    num_bedrooms = models.IntegerField(default=0)
    num_bathrooms = models.IntegerField(default=0)

    # add location field
    suburb = models.CharField(max_length=100, default='')
    state = models.CharField(default='NSW', max_length=50)
    country = models.CharField(default='Australia', max_length=50)

    def __str__(self):
        return self.accommodation_name

    def get_user(self):
        return self.user

    def get_accommodation_name(self):
        return self.accommodation_name

    def get_accommodation_description(self):
        return self.accommodation_description

    def get_house_rules(self):
        return self.house_rules

    def get_booking_rules(self):
        return self.booking_rules

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

    #--------------------------------

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

    #--------------------------------

    def delete_me(self):
        self.delete()

class Accomodation_Review(models.Model):

    advert = models.ForeignKey(Advertisement, related_name='accomodation_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

    def get_advertisement(self):
        return self.advert

    def get_rating(self):
        return self.rating

    def get_title(self):
        return self.title

    def get_message(self):
        return self.message

    #--------------------------------

    def set_rating(self, new_rating):
        u = Accomodation_Review.objects.get(id=self.id)
        u.rating = new_rating
        u.save()

    def set_title(self, new_title):
        u = Accomodation_Review.objects.get(id=self.id)
        u.title = new_title
        u.save()

    def set_message(self, new_message):
        u = Accomodation_Review.objects.get(id=self.id)
        u.message = new_message
        u.save()

    #--------------------------------

    def delete_me(self):
        self.delete()


class Amenities(models.Model):

    advert = models.ForeignKey(Advertisement, related_name='amenities', on_delete=models.CASCADE)
    feature = models.CharField(max_length=200)

    def __str__(self):
        return self.feature

    def get_advertisement(self):
        return self.advert

    def get_feature(self):
        return self.feature

    #--------------------------------

    def set_feature(self, new_feature):
        f = Amenties.objects.get(id=self.id)
        f.feature = new_feature
        f.save()

    #--------------------------------

    def delete_me(self):
        self.delete()


class PropertyImage(models.Model):

    advert = models.ForeignKey(Advertisement, related_name='property_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'accommodation_pics/')

    #--------------------------------

    def delete_me(self):
        self.delete()

class Event(models.Model):

    advert = models.ForeignKey(Advertisement, related_name='events', on_delete=models.CASCADE)

    start_day = models.DateField(u'Start day of the rent', help_text=u'Start day of the rent')
    start_day_start_time = models.TimeField(u'Starting time', help_text=u'Starting time')

    end_day = models.DateField(u'End day of the event', help_text=u'End day of the event')
    end_day_end_time = models.TimeField(u'Final time', help_text=u'Final time')

    booking_status = 'booked'

    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

    def check_overlap(self, fixed_start_day, fixed_start_day_start_time, fixed_end_day, fixed_end_day_end_time,
                      new_start_day, new_start_day_start_time, new_end_day, new_end_day_end_time):

        overlap = False
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
                                      ) and event.id != self.id:
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

    def get_advertisement(self):
        return self.advert

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

    #--------------------------------
#TODO need to check the validity when using these methods to modify the data
# currently it trivaly either modifies db or doesn't
# need to return some feed back to user.
# above case is valid when creating the event. Just nothing for editing the event.
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

    #--------------------------------

    def delete_me(self):
        self.delete()
