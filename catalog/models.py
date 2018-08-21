from __future__ import unicode_literals
from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse


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

class PropertyImage(models.Model):
    property = models.ForeignKey(Advertisement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField()

    #def __str__(self):
    #    return self.property.related_name

class Event(models.Model):
    property = models.ForeignKey(Advertisement, related_name='calendar', on_delete=models.CASCADE)
    day = models.DateField(u'Day of the event', help_text=u'Day of the event')
    start_time = models.TimeField(u'Starting time', help_text=u'Starting time')
    end_time = models.TimeField(u'Final time', help_text=u'Final time')
    notes = models.TextField(u'Textual Notes', help_text=u'Textual Notes', blank=True, null=True)

    class Meta:
        verbose_name = u'Scheduling'
        verbose_name_plural = u'Scheduling'

''' (there is a bug here, forgot to change back to gladys branch.
just leave this commented out till I fix it.)
    def check_overlap(self, fixed_start, fixed_end, new_start, new_end):
        overlap = False
        if new_start == fixed_end or new_end == fixed_start:    #edge case
            overlap = False
        elif (new_start >= fixed_start and new_start <= fixed_end) or (new_end >= fixed_start and new_end <= fixed_end): #innner limits
            overlap = True
        elif new_start <= fixed_start and new_end >= fixed_end: #outter limits
            overlap = True

        return overlap

    def get_absolute_url(self):
        url = reverse('admin:%s_%s_change' % (self._meta.app_label, self._meta.model_name), args=[self.id])
        return u'<a href="%s">%s</a>' % (url, str(self.start_time))

    def clean(self):
        if self.end_time <= self.start_time:
            raise ValidationError('Ending times must after starting times')

        events = Event.objects.filter(day=self.day)
        if events.exists():
            for event in events:
                if self.check_overlap(event.start_time, event.end_time, self.start_time, self.end_time):
                    raise ValidationError(
                        'There is an overlap with another event: ' + str(event.day) + ', ' + str(
                            event.start_time) + '-' + str(event.end_time))
'''
