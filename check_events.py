
"""

Script runs forever until terminated.
It continually checks if events are over yet.
If they are over, it will change the status of the event
from booked to finished.

To run this file:
python check_events.py &

"""
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone.settings")
# First run django.setup()
django.setup()

import time
from datetime import datetime
from catalog.models import Event

while True:

    events = Event.objects.all()

    today_date = datetime.today()
    today_date = str(today_date).split()
    today_date = datetime.strptime(today_date[0], "%Y-%m-%d").date()

    for e in events:
        if e.get_end_day() < today_date:
            print('changed', e.get_end_day())
            e.set_booking_status('finished')

    # 1 day = 86400 seconds
    # since our bookings are done one a per day basis
    # we only need to update the events once a day
    time.sleep(86000)
