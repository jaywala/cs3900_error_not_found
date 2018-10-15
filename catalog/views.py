
from django.http import *

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import Event, User_Profile, PropertyImage, PropertyRequest

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import EventSerializer, UserProfileSerializer
from catalog.serializers import PropertyImageSerializer, PropertyRequestSerializer

from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.db.models import Max

from .geo import position
from .haversine import haversine
from datetime import datetime, time
import math

#------------------------------User_Profile (booker, poster) ------------------------------#

def user_profile_get(request):
    """
    Give all the information related to the user profile based on email.
    (Model: User_Profile).
    """

    print('-----------> inside GET user_profile_get <-----------\n',
          'data given: ', request.GET, '\n')

    if 'email' in request.GET:
        email = request.GET['email']

        try:
            user = User_Profile.objects.get(email=email)
        except User_Profile.DoesNotExist:
            return HttpResponse(status=404)

        serializer = UserProfileSerializer(user)

        print('-----------> data given to frontend <-----------\n', \
              serializer.data, '\n------------------------')

        return JsonResponse(serializer.data)
    else:
        return HttpResponse(status=400)


def user_profile_update(request):
    """
    Updates User Profile data for the given email.
    (Model: User_Profile)
    """

    data = JSONParser().parse(request)

    email = data['body']['email']

    print('-----------> inside UPDATE user_profile <-----------\n',
          email, '\n------------------------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return HttpResponse(status=404)

    print('-----------> data to UPDATE <-----------\n', data, \
          '\n------------------------')

    new_email = data['body']['email']
    new_user_name = data['body']['nickname']
    new_name = data['body']['name']
    new_profile_pic = data['body']['picture']

    user.set_email(new_email)
    user.set_user_name(new_user_name)
    user.set_name(new_name)
    user.set_profile_pic(new_profile_pic)

    return HttpResponse(status=200)


def create_user(data):
    """
    Creates a new user profile.
    (Model: User_Profile)
    """

    email = data['body']['email']
    user_name = data['body']['nickname']
    name = data['body']['name']
    profile_pic = data['body']['picture']
    list_of_ads = ""
    list_of_rentals = ""
    list_of_posted_reviews = ""

    u = User_Profile(email=email,
                     user_name=user_name,
                     name=name,
                     profile_pic=profile_pic,
                     list_of_ads=list_of_ads,
                     list_of_rentals=list_of_rentals,
                     list_of_posted_reviews=list_of_posted_reviews,
                     )
    u.save()

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return False

    print('-----------> inside create_user, created user: <-----------\n', \
    email, '\n------------------------')

    return True


def is_loggedIn(request):
    """
    Checks if this user is registered in the database.
    If not, it creates a user.
    """

    data = JSONParser().parse(request)

    email = data['body']['email']

    print('-----------> inside is_loggedIn <-----------\n', email, \
          '\n------------------------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        is_created = create_user(data) # returns True or False
        if is_created:
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

    return HttpResponse(status=200)


#------------------------------Advertisement (poster) ------------------------------#

def advertisement_get(request):
    """
    Give all the ads for this user.
    (Model: Advertisement)
    """

    print('-----------> inside GET advertisement <-----------\n',
          'data given: ', request.GET, '\n')

    if 'email' in request.GET:
        email = request.GET['email']

        try:
            ad = Advertisement.objects.filter(poster=email)
        except Advertisement.DoesNotExist:
            return HttpResponse(status=404)

        serializer = AdvertisementSerializer(ad, many=True)

        print('-----------> data given to frontend <-----------\n', \
              serializer.data, '\n------------------------')

        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)


def advertisement_update(request):
    """
    Updates an advertisement's data.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    poster = data['body']['poster']
    ad_id = data['body']['ad_id']

    print('-----------> inside UPDATE advertisement <-----------\n', \
          'poster: ', poster, ', ad_id: ', ad_id, '\n------------------------')

    try:
        ad = Advertisement.objects.get(ad_id=ad_id, poster=poster)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    print('-----------> Found ad:\n', ad, '\n------------------------')

    accommodation_name = data['body']['title']
    accommodation_description = data['body']['summary']
    property_type = data['body']['propertyType']
    house_rules = "" #data['body']['house_rules']
    booking_rules = "" #data['body']['booking_rules']
    amenities = data['body']['amenities']
    base_price = data['body']['base_price'] 
    num_guests = data['body']['nGuests']
    num_bedrooms = data['body']['nBedrooms']
    num_bathrooms = data['body']['nBathrooms']
    address = data['body']['address']
    city = data['body']['city']
    zip_code = data['body']['zipCode']

    lat, long = 0, 0 #position(address)
    latitude = lat
    longitude = long

    ad.set_accommodation_name(accommodation_name)
    ad.set_accommodation_description(accommodation_description)
    ad.set_property_type(property_type)
    ad.set_house_rules(house_rules)
    ad.set_booking_rules(booking_rules)
    ad.set_amenities(amenities)
    ad.set_base_price(base_price)
    ad.set_num_guests(num_guests)
    ad.set_num_bedrooms(num_bedrooms)
    ad.set_num_bathrooms(num_bathrooms)
    ad.set_address(address)
    ad.set_city(city)
    ad.set_zip_code(zip_code)
    ad.set_latitude(latitude)
    ad.set_longitude(longitude)

    return HttpResponse(status=200)


def advertisement_create(request):
    """
    Create a new advertisement for this user.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    poster = data['user']['email']

    print('-----------> inside CREATE advertisement <-----------\n',
          poster, '\n------------------------')

    # Find the next ad_id for this user's ads
    u = User_Profile.objects.get(email=poster)
    #print(u.id)
    poster_id = u.id
    str_of_id = u.get_list_of_ads()
    if str_of_id == None or str_of_id == "":
        ad_id = 1 # this is the first ad this user is posting
    else:
        temp = str_of_id.split(',')
        # because the split() gives back this [''] so that's length 1
        # hence, the len(temp) > 1
        if len(temp) > 1:
            temp_list = []
            for i in temp:
                if i == '':
                    continue
                else:
                    temp_list.append(int(i))
            max_id = max(temp_list)
            new_id = max_id + 1
            ad_id = new_id
        else:
            ad_id = 1

    list_of_dict_of_images = data['images']
    id_counter = 1
    id_counter_str = ""
    for i in list_of_dict_of_images:
        base64 = i['base64']
        image = PropertyImage(image_id=id_counter,
                              ad_owner=poster,
                              ad_id=ad_id,
                              pic=base64
                             )
        image.save()
        id_counter_str = id_counter_str + str(id_counter) + ","
        id_counter += 1

    list_of_reviews = ""
    list_of_events = ""
    list_of_images = id_counter_str
    accommodation_name = data['body']['title']
    accommodation_description = data['body']['summary']
    property_type = data['body']['propertyType']
    house_rules = "" #data['body']['house_rules']
    booking_rules = "" #data['body']['booking_rules']
    amenities = data['body']['amenities']
    base_price = data['body']['base_price']
    num_guests = data['body']['nGuests']
    num_bedrooms = data['body']['nBedrooms']
    num_bathrooms = data['body']['nBathrooms']
    address = data['body']['address']
    city = data['body']['city']
    zip_code = data['body']['zipCode']

    #lat, long = position(address)
    latitude = 0 #lat
    longitude = 0 #long

    ad = Advertisement(
            ad_id = ad_id,
            poster = poster,
            poster_id = poster_id,
            list_of_reviews = list_of_reviews,
            list_of_events = list_of_events,
            list_of_images = list_of_images,
            accommodation_name = accommodation_name,
            accommodation_description = accommodation_description,
            property_type = property_type,
            house_rules = house_rules,
            booking_rules = booking_rules,
            amenities = amenities,
            base_price = base_price,
            num_guests = num_guests,
            num_bedrooms = num_bedrooms,
            num_bathrooms = num_bathrooms,
            address = address,
            city = city,
            zip_code = zip_code,
            latitude = latitude,
            longitude = longitude,
         )
    ad.save()

    temp_ad = Advertisement.objects.filter(ad_id=ad_id, poster=poster)

    print('-----------> Created ad: ', temp_ad, '\n------------------------')

    if temp_ad.exists() and len(temp_ad) == 1:

        # update the list_of_ads id for this user
        u = User_Profile.objects.get(email=poster)
        str_of_ads = u.get_list_of_ads()
        if str_of_ads == None or str_of_ads == "":
            new_str_of_ads = "1," # first ad this user has posted
        else:
            new_str_of_ads = str_of_ads + str(ad_id) + ','
        u.set_list_of_ads(new_str_of_ads)

        return HttpResponse(status=201)

    else:
        return HttpResponse(status=400)


def advertisement_delete(request):
    """
    Deletes this advertisement.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    poster = data['body']['poster']
    ad_id = data['body']['ad_id']

    print('-----------> inside DELETE advertisement <-----------\n',
          'poster: ', poster, '\n------------------------')

    ad = Advertisement.objects.filter(poster=poster, ad_id=ad_id)

    if ad.exists() and len(ad) == 1:

        ad.delete()

        # delete ad_id from user's list_of_ads
        u = User_Profile.objects.get(email=poster)
        str_of_ads = u.get_list_of_ads()
        if str_of_ads == None or str_of_ads == "":
            new_list_of_ads = ""
        else:
            str_list_of_ads = str_of_ads.split(',')
            new_list = []
            for i in str_list_of_ads:
                if i == '':
                    continue
                elif i == str(ad_id):
                    # delete the ad_id so we don't add to new_list
                    continue
                else:
                    new_list.append(i)

            new_list_of_ads = '' # contruct the string again to put back into db
            for i in new_list:
                new_list_of_ads = new_list_of_ads + i + ','
        u.set_list_of_ads(new_list_of_ads)

        # delete all instances of this ad's reviews
        r = list(Accommodation_Review.objects.filter(ad_id=ad_id, ad_owner=poster))
        for j in r:
            j.delete()

        # delete all instances of this ad's events
        e = list(Event.objects.filter(ad_id=ad_id, ad_owner=poster))
        for j in e:
            j.delete()

        # delete all instances of this ad's property images
        i = list(PropertyImage.objects.filter(ad_id=ad_id, ad_owner=poster))
        for j in i:
            j.delete()

        print('-----------> If empty list ad is deleted <-----------\n',
              ad, '\n------------------------')

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


#------------------------------Advertisement Reviews (booker) ------------------------------#

def review_get(request):
    """
    Give all reviews this advertisement's owns,
    identified by ad_owner and ad_id.
    (Model: Accommodation_Review)
    """

    print('-----------> inside GET Review <-----------\n',
          'data given: ', request.GET, '\n')

    if 'email' in request.GET and 'ad_id' in request.GET:
        ad_owner = request.GET['email']
        ad_id = request.GET['ad_id']

        try:
            rev = Accommodation_Review.objects.filter(ad_owner=ad_owner, ad_id=ad_id)
        except Accommodation_Review.DoesNotExist:
            return HttpResponse(status=404)

        serializer = AccommodationReviewSerializer(rev, many=True)

        print('-----------> data given to frontend <-----------\n', \
              serializer.data, '\n------------------------')

        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)


def review_create(request):
    """
    Create a new review for this advertisement,
    identified by ad_id and ad_owner, reviewer.
    The reviewer is the person currently logged in.
    (Model: Advertisement_Review)
    """

    data = JSONParser().parse(request)

    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    reviewer = data['user']['email']

    print('-----------> inside CREATE Review <-----------\n',
          'ad_owner: ', ad_owner, ', ad_id: ', ad_id,
          ', reviewer: ', reviewer, '\n------------------------')

    # Find the next rev_id for this ads's review
    u = Advertisement.objects.get(ad_id=ad_id, poster=ad_owner)
    str_of_id = u.get_rev_ids()
    if str_of_id == None or str_of_id == "":
        rev_id = 1 # this is the first review for this ad
    else:
        temp = str_of_id.split(',')
        temp_list = []
        for i in temp:
            if i == '':
                continue
            else:
                temp_list.append(int(i))
        max_id = max(temp_list)
        new_id = max_id + 1
        rev_id = new_id

    rating = data['body']['rating']
    message = data['body']['message']

    review = Accommodation_Review(
            rev_id=rev_id,
            ad_owner=ad_owner,
            ad_id=ad_id,
            reviewer=reviewer,
            rating=rating,
            message=message,
            )
    review.save()

    temp_review = Accommodation_Review.objects.filter(rev_id=rev_id, ad_id=ad_id, ad_owner=ad_owner)

    if temp_review.exists() and len(temp_review) == 1:

        # Adding review ID to this advertisement's list_of_reviews
        a = Advertisement.objects.get(poster=ad_owner, ad_id=ad_id)
        str_of_rev_ids = a.get_rev_ids()
        if str_of_rev_ids == None or str_of_rev_ids == "":
            new_str_of_rev = str(rev_id) + ',' # first review for this ad
        else:
            new_str_of_rev = str_of_rev_ids + str(rev_id) + ','
        a.set_rev_ids(new_str_of_rev)

        # update user profile list_of_posted_reviews
        u = User_Profile.objects.get(email=reviewer)
        str_of_posted_reviews = u.get_list_of_posted_reviews()
        # string format: (ad_owner, ad_id, review_id);
        if str_of_posted_reviews == None or str_of_posted_reviews == "":
            # first posted review for this user
            new_str_of_posted_revs = '(' + ad_owner + ',' + str(ad_id) + ',' + str(review_id) + ');'
        else:
            new_str_of_posted_revs = str_of_posted_reviews + \
                '(' + ad_owner + ',' + str(ad_id) + ',' + str(review_id) + ');'
        u.set_list_of_posted_reviews(new_str_of_posted_revs)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


def review_update(request):
    """
    Updates Advertisement Review for the given rev_id, ad_id and ad_owner.
    Only the reviewer should be updating.
    (Model: Advertisement_Review)
    """

    data = JSONParser().parse(request)

    rev_id = data['body']['rev_id']
    ad_id = data['body']['ad_id']
    ad_owner = data['body']['ad_owner']

    reviewer = data['user']['email']

    print('-----------> inside UPDATE Review <-----------\n', \
          'ad_owner: ', ad_owner, ', ad_id: ', ad_id,         \
          'rev_id: ', rev_id, ', reviewer: ', reviewer,       \
          '\n------------------------')

    review = Accommodation_Review.objects.get(rev_id=rev_id,
                                              ad_id=ad_id,
                                              ad_owner=ad_owner)

    rating = data['body']['rating']
    message = data['body']['message']

    review.set_rating(rating)
    review.set_message(message)

    return HttpResponse(status=200)


def review_delete(request):
    """
    Deletes the advertisement review for the given rev_id,
    ad_id and ad_owner.
    Only the reviewer should be deleting review.
    (Model: Advertisement_Review)
    """

    data = JSONParser().parse(request)

    rev_id = data['body']['rev_id']
    ad_id = data['body']['ad_id']
    ad_owner = data['body']['ad_owner']

    reviewer = data['user']['email']

    print('-----------> inside DELETE Review <-----------\n', \
          'ad_owner: ', ad_owner, ', ad_id: ', ad_id,         \
          'rev_id: ', rev_id, ', reviewer: ', reviewer,       \
          '\n------------------------')

    rev = Accommodation_Review.objects.filter(rev_id=rev_id, ad_id=ad_id,
                                              ad_owner=ad_owner)

    if rev.exists() and len(rev) == 1:

        rev.delete()

        # deleting the rev_id from this ads list_of_reviews
        a = Advertisement.objects.get(poster=ad_owner, ad_id=ad_id)
        str_of_rev = a.get_rev_ids()
        if str_of_rev == None or str_of_rev == "":
            new_list_of_rev = ''
        else:
            str_list_of_rev = str_of_rev.split(',')
            new_list = []
            for i in str_list_of_rev:
                if i == '':
                    continue
                elif i == str(rev_id):
                    # delete the rev_id so we don't add to new_list
                    continue
                else:
                    new_list.append(i)

            new_list_of_rev = '' #contruct the string again to put back into db
            for i in new_list:
                new_list_of_rev = new_list_of_rev + i + ','
        a.set_rev_ids(new_list_of_rev)

        # delete review from User_Profile list_of_posted_reviews
        a = User_Profile.objects.get(email=reviewer)
        str_of_posted_revs = a.get_list_of_posted_reviews()
        if str_of_posted_revs == None or str_of_posted_revs == "":
            new_list_of_posted_revs = ''
        else:
            str_list_of_posted_revs = str_of_posted_revs.split(';')
            new_list = []
            # string format: (ad_owner, ad_id, rev_id);
            str_to_delete = '(' + ad_owner + ',' + str(ad_id) + ',' + str(rev_id) + ');'
            for i in str_list_of_posted_revs:
                if i == '':
                    continue
                elif i == str_to_delete:
                    # delete the rental so we don't add to list
                    continue
                else:
                    new_list.append(i)

            new_list_of_posted_revs = ''
            # contruct the string again to put back into db
            for i in new_list:
                new_list_of_posted_revs = new_list_of_posted_revs + i + ';'
        a.set_list_of_posted_reviews(new_list_of_posted_revs)

        print('-----------> If deleted this should be empty ', rev, \
              '\n------------------------')

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


#------------------------------Advertisement Events (booker) ------------------------------#

def event_get(request):
    """
    Give events this advertisement owns, identified by poster and ad_id.
    (Model: Event)
    """

    print('-----------> inside GET Event <-----------\n',
          'data given: ', request.GET, '\n')

    if 'email' in request.GET and 'ad_id' in request.GET:
        poster = request.GET['email']
        ad_id = request.GET['ad_id']

        try:
            event = Event.objects.filter(ad_owner=poster, ad_id=ad_id)
        except Event.DoesNotExist:
            return HttpResponse(status=404)

        serializer = EventSerializer(event, many=True)

        print('-----------> data given to frontend <-----------\n', \
              serializer.data, '\n------------------------')

        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)


def event_create(request):
    """
    Create a new event for this advertisement,
    identified by poster_id (integer), ad_id, and booker (email).
    Booker is the user that is currently logged in.
    (Model: Event)
    """

    data = JSONParser().parse(request)

    poster_id = data['body']['poster_id']
    ad_id = data['body']['ad_id']

    booker = data['user']['email']

    print('-----------> inside CREATE Event <-----------\n poster_id: ', \
          poster_id, '\n booker: ', booker, '\n------------------------')

    u = Advertisement.objects.get(ad_id=ad_id, poster_id=poster_id)
    ad_owner = u.get_poster()

    # Find the next event id for this event
    str_of_id = u.get_event_ids()
    if str_of_id == None or str_of_id == "":
        event_id = 1 # this is the first event for this ad
    else:
        temp = str_of_id.split(',')
        temp_list = []
        for i in temp:
            if i =='':
                continue
            else:
                temp_list.append(int(i))
        max_id = max(temp_list)
        new_id = max_id + 1
        event_id = new_id

    checkIn = data['detail']['start_day'].split('T') # '2018-09-30T14:00:00.000Z'
    checkout = data['detail']['end_day'].split('T')  # only want 2018-09-30

    start_day =  datetime.strptime(checkIn[0], "%Y-%m-%d").date()
    start_day_start_time = datetime.strptime('00:00:00', "%H:%M:%S").time() # default midnight
    end_day = datetime.strptime(checkout[0], "%Y-%m-%d").date()
    end_day_end_time = datetime.strptime('00:00:00', "%H:%M:%S").time() # default midnight
    booking_status = "booked"
    notes = "number of guests " + str(data['detail']['guest'])

    event = Event(
            event_id=event_id,
            ad_owner=ad_owner,
            ad_id=ad_id,
            booker=booker,
            start_day=start_day,
            start_day_start_time=start_day_start_time,
            end_day=end_day,
            end_day_end_time=end_day_end_time,
            booking_status=booking_status,
            notes=notes
            )
    event.save()

    temp_event = Event.objects.filter(event_id=event_id, ad_owner=ad_owner, ad_id=ad_id)

    if temp_event.exists() and len(temp_event) == 1:

        # update ad's list_of_events
        a = Advertisement.objects.get(ad_id=ad_id, poster=ad_owner)
        str_of_event_ids = a.get_event_ids()
        if str_of_event_ids == None or str_of_event_ids == "":
            new_str_of_events = str(event_id) + ',' # first review for this ad
        else:
            new_str_of_events = str_of_event_ids + str(event_id) + ','
        a.set_event_ids(new_str_of_events)

        # update user profile list_of_rentals
        u = User_Profile.objects.get(email=booker)
        str_of_rentals = u.get_list_of_rentals()
        # string format: (ad_owner, ad_id, event_id);
        if str_of_rentals == None or str_of_rentals == "":
            # first rental for this booker
            new_str_of_rentals = '(' + ad_owner + ',' + str(ad_id) + ',' + str(event_id) + ');'
        else:
            new_str_of_rentals = str_of_rentals + \
                '(' + ad_owner + ',' + str(ad_id) + ',' + str(event_id) + ');'
        u.set_list_of_rentals(new_str_of_rentals)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


def event_update(request):
    """
    Updates event, identified by ad_owner (email)
    ad_id and event_id.
    (Model: Event)
    """

    data = JSONParser().parse(request)

    event_id = data['body']['event_id']
    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    booker = data['user']['email']

    print('-----------> inside UPDATE Event <-----------\n ad_owner: ', \
          ad_owner, '\n booker: ', booker, '\n------------------------')

    event = Event.objects.filter(event_id=event_id, ad_owner=ad_owner, ad_id=ad_id)

    if event.exists() and len(event) == 1:

        event = event[0]

        checkIn = data['body']['start_day'].split('T') # '2018-09-30T14:00:00.000Z'
        checkout = data['body']['end_day'].split('T')  # only want 2018-09-30

        start_day =  datetime.strptime(checkIn[0], "%Y-%m-%d").date()
        start_day_start_time = datetime.strptime('00:00:00', "%H:%M:%S").time() # default midnight
        end_day = datetime.strptime(checkout[0], "%Y-%m-%d").date()
        end_day_end_time = datetime.strptime('00:00:00', "%H:%M:%S").time() # default midnight
        booking_status = "booked"
        notes = "number of guests " + str(data['body']['guest'])

        event.set_start_day(start_day)
        event.set_start_day_start_time(start_day_start_time)
        event.set_end_day(end_day)
        event.set_end_day_end_time(end_day_end_time)
        event.set_booking_status(booking_status)
        event.set_notes(notes)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


def event_delete(request):
    """
    Deletes the event with event_id, ad_owner and ad_id.
    (Model: Event)
    """

    data = JSONParser().parse(request)

    event_id = data['body']['event_id']
    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    booker = data['user']['email']

    print('-----------> inside DELETE event <-----------\n', event_id, \
          '\n------------------------')

    event = Event.objects.filter(event_id=event_id, ad_owner=ad_owner, ad_id=ad_id)

    if event.exists() and len(event) == 1:

        event.delete()

        # delete the event_id from Advertisement list_of_events
        a = Advertisement.objects.get(poster=ad_owner, ad_id=ad_id)
        str_of_events = a.get_event_ids()
        if str_of_events == None or str_of_events == "":
            new_list_of_events = ''
        else:
            str_list_of_events = str_of_events.split(',')
            new_list = []
            for i in str_list_of_events:
                if i == '':
                    continue
                elif i == str(event_id):
                    # delete the event_id so we don't add to list
                    continue
                else:
                    new_list.append(i)

            new_list_of_events = '' #contruct the string again to put back into db
            for i in new_list:
                new_list_of_events = new_list_of_events + i + ','

        a.set_event_ids(new_list_of_events)

        # delete rental from User_Profile list_of_rentals
        a = User_Profile.objects.get(email=booker)
        str_of_rentals = a.get_list_of_rentals()
        if str_of_rentals == None or str_of_rentals == "":
            new_list_of_rentals = ''
        else:
            str_list_of_rentals = str_of_rentals.split(';')
            new_list = []
            # string format: (ad_owner, ad_id, event_id);
            str_to_delete = '(' + ad_owner + ',' + str(ad_id) + ',' + str(event_id) + ');'
            for i in str_list_of_rentals:
                if i == '':
                    continue
                elif i == str_to_delete:
                    # delete the rental so we don't add to list
                    continue
                else:
                    new_list.append(i)

            new_list_of_rentals = '' # contruct the string again to put back into db
            for i in new_list:
                new_list_of_rentals = new_list_of_rentals + i + ';'

        a.set_list_of_rentals(new_list_of_rentals)


        print('-----------> If deleted this is an empty list ', event,
              '\n------------------------')

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


#------------------------------ Images ------------------------------#

def image_get(request):
    """
    Give all the images for this advertisement.
    (Model: PropertyImage)
    """

    print('-----------> inside GET Image <-----------\n',
          'data given: ', request.GET, '\n')

    if 'email' in request.GET and 'ad_id' in request.GET:
        poster = request.GET['email']
        ad_id = request.GET['ad_id']

        try:
            images = PropertyImage.objects.filter(ad_owner=poster, ad_id=ad_id)
        except PropertyImage.DoesNotExist:
            return HttpResponse(status=404)

        serializer = PropertyImageSerializer(images, many=True)

        print('-----------> data given to frontend <-----------\n', \
              serializer.data, '\n------------------------')

        return JsonResponse(serializer.data, safe=False)
    else:
        return HttpResponse(status=400)


def image_create(request):
    """
    Create a new image for this advertisement,
    identified by ad_owner and ad_id.
    (Model: PropertyImage)
    """

    data = JSONParser().parse(request)

    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside CREATE image <-----------\n', ad_owner, \
          '\n------------------------')

    # Find the next image id for this ad
    u = Advertisement.objects.get(ad_id=ad_id, poster=ad_owner)
    str_of_id = u.get_image_ids()
    if str_of_id == None or str_of_id == "":
        image_id = 1 # this is the first image for this ad
    else:
        temp = str_of_id.split(',')
        temp_list = []
        for i in temp:
            if i == '':
                continue
            else:
                temp_list.append(int(i))
        max_id = max(temp_list)
        new_id = max_id + 1
        image_id = new_id

    pic = data['body']['pic']

    image = PropertyImage(
            image_id=image_id,
            ad_owner=ad_owner,
            ad_id=ad_id,
            pic=pic,
            )
    image.save()

    temp_image = PropertyImage.objects.filter(image_id=image_id, ad_owner=ad_owner, ad_id=ad_id)

    if temp_image.exists() and len(temp_image) == 1:

        # add this image id to ad's list_of_images
        a = Advertisement.objects.get(ad_id=ad_id, poster=ad_owner)
        str_of_image_ids = a.get_image_ids()
        if str_of_image_ids == None or str_of_image_ids == "":
            new_str_of_images = str(image_id) + ',' # first image for this ad
        else:
            new_str_of_images = str_of_image_ids + str(image_id) + ','
        a.set_image_ids(new_str_of_images)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


def image_update(request):
    """
    Updates image, identified by image_id, poster (email) and ad_id.
    (Model: PropertyImage)
    """

    data = JSONParser().parse(request)

    image_id = data['body']['image_id']
    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside UPDATE image <-----------\n', ad_owner, \
          '\n------------------------')

    image = PropertyImage.objects.filter(image_id=image_id, ad_owner=ad_owner, ad_id=ad_id)

    if image.exists() and len(image) == 1:

        image = image[0]

        pic = data['body']['pic']

        image.set_pic(pic)

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=404)


def image_delete(request):
    """
    Deletes the image with image_id, ad_owner and ad_id.
    (Model: PropertyImage)
    """

    data = JSONParser().parse(request)

    image_id = data['body']['image_id']
    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside DELETE event <-----------\n', image_id, \
          '\n------------------------')

    image = PropertyImage.objects.filter(image_id=image_id, ad_owner=ad_owner, ad_id=ad_id)

    if image.exists() and len(image) == 1:

        image.delete()

        # delete the image id from this ads list_of_images
        a = Advertisement.objects.get(poster=ad_owner, ad_id=ad_id)
        str_of_image = a.get_image_ids()
        if str_of_image == None or str_of_image == "":
            new_list_of_images = ''
        else:
            str_list_of_images = str_of_image.split(',')
            new_list = []
            for i in str_list_of_images:
                if i == '':
                    continue
                elif i == str(image_id):
                    # delete the event_id so we don't add to list
                    continue
                else:
                    new_list.append(i)

            new_list_of_images = '' # contruct the string again to put back into db
            for i in new_list:
                new_list_of_images = new_list_of_images + i + ','

        a.set_image_ids(new_list_of_images)

        print('-----------> If deleted this is an empty list ', image, \
              '\n------------------------')

        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


#------------------------------ General Views ------------------------------#

def get_single_ad(request):
    """
    Gives ONE ad, identified by email and ad_id.
    With the ad, it also gives the ad's images, events, and reviews.
    (Model: Advertisement)
    """

    print('-----------> inside GET single_ad <-----------\n',
          'data given: ', request.GET, '\n')

    if 'poster_id' in request.GET and 'ad_id' in request.GET:
        poster_id = request.GET['poster_id']
        ad_id = request.GET['ad_id']

        ad = Advertisement.objects.get(poster_id=poster_id, ad_id=ad_id)
        poster = ad.get_poster()

        # Get image id's from the ad model
        image_ids_str = ad.get_image_ids()
        image_ids = []
        for i in image_ids_str.split(','):
            if i == '':
                continue
            else:
                image_ids.append(int(i))
        print('image_ids ', image_ids)

        # Get event ids
        event_ids_str = ad.get_event_ids()
        event_ids = []
        for i in event_ids_str.split(','):
            if i == '':
                continue
            else:
                event_ids.append(int(i))
        print('event_ids ', event_ids)

        # Get review ids
        rev_ids_str = ad.get_rev_ids()
        rev_ids = []
        for i in rev_ids_str.split(','):
            if i == '':
                continue
            else:
                rev_ids.append(int(i))
        print('rev_ids ', rev_ids)

        # Contruct JSON with both the SINGLE ad and
        # all it's images, events, reviews
        ad = Advertisement.objects.get(poster=poster, ad_id=ad_id)
        adSerializer = AdvertisementSerializer(ad).data

        images = PropertyImage.objects.filter(ad_owner=poster, ad_id=ad_id)
        imageSerializer = PropertyImageSerializer(images, many=True).data

        events = Event.objects.filter(ad_owner=poster, ad_id=ad_id)
        eventSerializer = EventSerializer(events, many=True).data

        review = Accommodation_Review.objects.filter(ad_owner=poster, ad_id=ad_id)
        reviewSerializer = AccommodationReviewSerializer(review, many=True).data

        querylist = [adSerializer, imageSerializer, eventSerializer, reviewSerializer]

        #print(querylist)

        return JsonResponse(querylist, safe=False)
    else:
        return HttpResponse(status=400)


def get_all_ads(request):
    """
    Gets all the ads in the database.
    (Model: Advertisement)
    """

    print('-----------> inside get_all_ads <-----------')

    try:
        a = Advertisement.objects.all()
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    serializer = AdvertisementSerializer(a, many=True)

    #print('-----------> data given to frontend <-----------\n', \
    #      serializer.data, '\n------------------------')

    return JsonResponse(serializer.data, safe=False)


def get_users_ads(request):
    """
    Gets all the ads, images, events, and reviews for this user.
    """

    print('-----------> inside GET users_ads <-----------\n',
          'data given: ', request.GET, '\n')

    if 'email' in request.GET:
        email = request.GET['email']

        try:
            ads = Advertisement.objects.filter(poster=email)
        except Advertisement.DoesNotExist:
            return HttpResponse(status=404)

        querylist = []

        for a in ads:
            adSerializer = AdvertisementSerializer(a).data

            images = PropertyImage.objects.filter(ad_owner=a.poster, ad_id=a.ad_id)
            imagesSerializer = PropertyImageSerializer(images, many=True).data

            events = Event.objects.filter(ad_owner=a.poster, ad_id=a.ad_id)
            eventsSerializer = EventSerializer(events, many=True).data

            reviews = Accommodation_Review.objects.filter(ad_owner=a.poster, ad_id=a.ad_id)
            reviewsSerializer = AccommodationReviewSerializer(reviews, many=True).data

            temp_dict = {
                'ad': adSerializer,
                'images': imagesSerializer,
                'events': eventsSerializer,
                'reviews': reviewsSerializer
            }
            querylist.append(temp_dict)

        #print('-----------> data given to frontend <-----------\n', \
        #      querylist, '\n------------------------')

        return JsonResponse(querylist, safe=False)
    else:
        return HttpResponse(status=400)


def get_prop_requests(request):
    """
    Gets all property requests.
    (Model: PropertyRequest)
    """

    print('-----------> inside GET prop_requests <-----------')

    try:
        a = PropertyRequest.objects.all()
    except PropertyRequest.DoesNotExist:
        return HttpResponse(status=404)

    serializer = PropertyRequestSerializer(a, many=True)

    print('-----------> data given to frontend <-----------\n', \
          serializer.data, '\n------------------------')

    return JsonResponse(serializer.data, safe=False)


def create_prop_request(request):
    """
    Creates a property request.
    (Model: PropertyRequest)
    """

    data = JSONParser().parse(request)

    name = data['body']['name']
    email = data['body']['email']
    text = data['body']['detail']

    p = PropertyRequest(name=name, email=email, text=text)
    p.save()

    # this allows frontend view to refesh with new request
    try:
        a = PropertyRequest.objects.all()
    except PropertyRequest.DoesNotExist:
        return HttpResponse(status=404)

    serializer = PropertyRequestSerializer(a, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)


def update_prop_request(request):
    """
    Updates a property request.
    (Model: PropertyRequest)
    """

    print('-----------> inside UPDATE property request <-----------\n')

    data = JSONParser().parse(request)

    name = data['body']['name']
    email = data['body']['email']
    text = data['body']['detail']

    id = data['body']['id']

    p = PropertyRequest.objects.get(pk=id)
    p.set_name(name)
    p.set_email(email)
    p.set_text(text)

    try:
        a = PropertyRequest.objects.all()
    except PropertyRequest.DoesNotExist:
        return HttpResponse(status=404)

    serializer = PropertyRequestSerializer(a, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)


def delete_prop_request(request):

    data = JSONParser().parse(request)
    id = data['body']['id']

    p = PropertyRequest.objects.get(pk=id)
    p.delete()

    try:
        a = PropertyRequest.objects.all()
    except PropertyRequest.DoesNotExist:
        return HttpResponse(status=404)

    serializer = PropertyRequestSerializer(a, many=True)

    return JsonResponse(serializer.data, safe=False, status=200)


#------------------------------Search Module Views------------------------------#

def search(request):
    """
    Searches through all the ads and returns the ads that satisfies the parameters.
    (Model: Advertisement)
    """

    if 'dateOne' in request.GET:
        checkIn = request.GET['dateOne']
    if 'dateTwo' in request.GET:
        checkOut = request.GET['dateTwo']
    if 'where' in request.GET:
        location = request.GET['where']
    if 'guests' in request.GET:
        nGuests = request.GET['guests']
    if 'minPrice' in request.GET:
        minPrice = request.GET['minPrice']
    if 'maxPrice' in request.GET:
        maxPrice = request.GET['maxPrice']
    if 'distance' in request.GET:
        distance = request.GET['distance']

    print('-----------> inside GET search <-----------\n',
          'checkIn: ', checkIn,
          '\ncheckOut: ', checkOut,
          '\nlocation: ', location,
          '\nnGuests: ', nGuests,
          '\nminPrice: ', minPrice,
          '\nmaxPrice: ', maxPrice,
          '\ndistance', distance,
          '\n'
         )

    if nGuests == "":
        nGuests = 0
    if minPrice == "":
        minPrice = 0
    if maxPrice == "":
        maxPrice =  100000

    ads = Advertisement.objects.filter(num_guests__gte = nGuests,
                                       base_price__gte = minPrice,
                                       base_price__lte = maxPrice)
    pk_list = []

    for a in ads:

        search_distance = None
        if location != "null" and location != "":

            search_latitude, search_longitude = 0, 0 #position(location)
            search_loc = (search_longitude, search_latitude)

            ads_latitude = a.get_latitude()
            ads_longitude = a.get_longitude()
            ads_loc = (ads_longitude, ads_latitude)

            if distance != "null" and distance != "":
                search_distance = float(distance)
            else:
                # if no distance given, default search is 10 km
                search_distance = 10


            # calculates the distance between two long/lat
            # coordnate pairs in km.
            dist_apart = haversine(ads_loc, search_loc)

        if search_distance != None:
            if dist_apart > search_distance: # too far away
                continue # don't add this ad to search results

        is_clashing = None
        if checkIn != "null" and checkOut != "null" and checkIn != "" and checkOut != "":
            event_ids = a.get_event_ids()
            # convert string into list
            event_ids = event_ids.split(',')

            is_clashing = False
            for i in event_ids:
                if i == "":
                    continue
                i = int(i)
                e = Event.objects.get(event_id=i, ad_owner=a.poster, ad_id=a.ad_id)

                checkIn = datetime.strptime(str(checkIn), "%Y-%m-%d").date()
                checkOut = datetime.strptime(str(checkOut), "%Y-%m-%d").date()

                if checkIn >= e.get_start_day() and checkIn <= e.get_end_day():
                    is_clashing = True
                elif checkIn == e.get_start_day() or checkIn == e.get_end_day():
                    is_clashing = True
                elif checkOut >= e.get_start_day() and checkOut <= e.get_end_day():
                    is_clashing = True
                elif checkOut == e.get_start_day() or checkOut == e.get_end_day():
                    is_clashing = True

            if not is_clashing:
                # if it's not clashing then is_clashing would equal False
                # so not is_clashing equals true
                pk_list.append(a.pk)

        if is_clashing == None: # checkIn & checkOut was not given
            pk_list.append(a.pk)

    # here we use the actual primary keys given buy the database
    suitable_ads = Advertisement.objects.filter(pk__in=pk_list)
    #adSerializer = AdvertisementSerializer(suitable_ads, many=True)

    querylist = []
    for a in suitable_ads:
        ad = Advertisement.objects.get(poster=a.poster, ad_id=a.ad_id)
        adSerializer = AdvertisementSerializer(ad).data
        images = PropertyImage.objects.filter(ad_owner=a.poster, ad_id=a.ad_id)
        imSerializer = PropertyImageSerializer(images, many=True).data
        querylist.append(adSerializer)
        querylist.append(imSerializer)

    #print(querylist)
    print('DONE SEARCHING')
    return JsonResponse(querylist, safe=False)


#------------------------------Booking Module Views------------------------------#

def bookers_bookings(request):
    """
    Gives all the bookings that this user has.
    (Model: Event)
    """

    print('-----------> inside bookers_bookings <-----------\n')

    if 'booker' in request.GET:
        booker = request.GET['booker']

        print('BOOKER: ', booker, '\n')

        u = User_Profile.objects.get(email=booker)

        # string format: (ad_owner, ad_id, event_id);
        str_of_bookings = u.get_list_of_rentals()
        list_of_bookings = str_of_bookings.split(';')

        event_pks = []
        for i in list_of_bookings:

            str_event = i.split(',')
            ad_owner = str_event[0]
            ad_id = str_event[1]
            event_id = str_event[2]

            e = Event.objects.get(event_id=event_id, ad_owner=ad_owner,
                                  ad_id=ad_id)
            event_pks.append(e.pk)

        bookers_events = Event.objects.filter(pk__in=event_pks)

        eventSerializer = EventSerializer(bookers_events, many=True)

        return JsonResponse(eventSerializer.data, safe=False)
    else:
        return HttpResponse(status=400)


#------------------------------Test Views------------------------------#

def user_detail(request, pk):
    """
    Shows JSON in browser of a particular user.
    """

    try:
        ad = User_Profile.objects.get(pk=pk)
    except User_Profile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserProfileSerializer(ad)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(ad, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ad.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)


def advertisement_detail(request, pk):
    """
    Shows JSON in browser of a particular ad.
    """

    try:
        ad = Advertisement.objects.get(pk=pk)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(ad)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdvertisementSerializer(ad, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ad.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)


def review_detail(request, pk):
    """
    Shows JSON in browser of a particular review.
    """

    try:
        ad = Accommodation_Review.objects.get(pk=pk)
    except Accommodation_Review.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AccommodationReviewSerializer(ad)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccommodationReviewSerializer(ad, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ad.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)


def event_detail(request, pk):
    """
    Shows JSON in browser of a particular event.
    """

    try:
        ad = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventSerializer(ad)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventSerializer(ad, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ad.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)


def image_detail(request, pk):
    """
    Shows JSON in browser of a particular image.
    """

    try:
        im = PropertyImage.objects.get(pk=pk)
    except PropertyImage.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PropertyImageSerializer(im)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PropertyImageSerializer(im, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        im.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)


def public(request):
    print("hello+",request.body)
    return HttpResponse("You don't need to be authenticated to see this")


def private(request):
    print("hello+",request.body)
    return HttpResponse("You should not see this message if not authenticated!")
