"""
# UNUSED CODE
def check_overlap(self, fixed_start_day, fixed_start_day_start_time, fixed_end_day, fixed_end_day_end_time,
                  new_start_day, new_start_day_start_time, new_end_day, new_end_day_end_time, event):
    overlap = False
    if self.event_id != event.event_id and self.ad_id != event.ad_id and self.ad_owner != event.ad_owner:
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
                     ) + ', ' + 'old event --> event ' + str(event.notes) )
                    #'There is an overlap with another event: ' + str(event.start_day) + ', ' + str(
                    #    event.start_day_start_time) + '-' + str(event.end_day) + ', ' + str(event.end_day_end_time))

def check_validity(self, pk_actual_event):

    if self.start_day > self.end_day:
        return False
    if self.start_day == self.end_day and self.start_day_start_time >= self.end_day_end_time:
        return False

    events = Event.objects.all()
    if events.exists():
        for event in events:
            if self.check_overlap(event.start_day, event.start_day_start_time, event.end_day, event.end_day_end_time,
                                  self.start_day, self.start_day_start_time, self.end_day, self.end_day_end_time
                                  , event) and event.id != self.id and event.id != pk_actual_event:
                return False
    return True
"""
