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
'''
    def get_user_name(self):
        return self.user_name

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def set_name(primary_key, new_name):
        u = Catalog.objects.get(id=primary_key)
        u.name = name
        u.save(['name'])
'''


class User_Review(models.Model):

    user = models.ForeignKey(User_Profile, related_name='user_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


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

    suburb = models.CharField(max_length=100, default='')
    state = models.CharField(default='NSW', max_length=50)
    country = models.CharField(default='Australia', max_length=50)

    def __str__(self):
        return self.accommodation_name


class Accomodation_Review(models.Model):

    advert = models.ForeignKey(Advertisement, related_name='accomodation_reviews', on_delete=models.CASCADE)
    rating = models.IntegerField()
    title = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class Amenities(models.Model):

    advert = models.ForeignKey(Advertisement, related_name='amenities', on_delete=models.CASCADE)
    feature = models.CharField(max_length=200)

    def __str__(self):
        return self.feature


class PropertyImage(models.Model):

    advert = models.ForeignKey(Advertisement, related_name='property_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'accommodation_pics/')


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
