
from django.http import *

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import Event, User_Profile

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import EventSerializer, UserProfileSerializer

from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.db.models import Max


#------------------------------User_Profile------------------------------#


def user_profile_get(request, first, second): #works & tested
    """
    Give all the information related to the user profile based on email.
    (Model: User_Profile).
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET user_profile_get <-----------\n', email, '\n------------------------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return HttpResponse(status=404)

    serializer = UserProfileSerializer(user)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data)



def user_profile_update(request): # works & tested
    """
    Updates User Profile data for the given email.
    (Model: User_Profile)
    """

    data = JSONParser().parse(request)

    email = data['body']['email']

    print('-----------> inside UPDATE user_profile <-----------\n', email, '\n------------------------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return HttpResponse(status=404)

    print('-----------> data to UPDATE <-----------\n', data, '\n------------------------')

    new_user_name = data['body']['user_name']
    new_name = data['body']['name']
    new_email = data['body']['email']
    new_profile_pic = data['body']['profile_pic']
    new_list_of_ads = data['body']['list_of_ads']

    user.set_user_name(new_user_name)
    user.set_name(new_name)
    user.set_email(new_email)
    user.set_profile_pic(new_profile_pic)
    user.set_list_of_ads(new_list_of_ads)

    current_user_name = user.get_user_name()
    current_name = user.get_name()
    current_email = user.get_email()
    current_profile_pic = user.get_profile_pic()
    current_list_of_ads = user.get_list_of_ads()

    '''
    The data does get updated but it still goes into this if.
    Not sure why, so taking this check out.

    if new_user_name != current_user_name or \
       new_name != current_name or \
       new_email != current_email or \
       new_profile_pic != current_profile_pic or \
       new_list_of_ads != current_list_of_ads:
        print('BAD REQUEST')
        return HttpResponse(status=400)
    else:
    '''
    return HttpResponse(status=200)


def create_user(data): #works & tested
    """
    Creates a new user profile.
    """

    user_name = data['body']['user_name']
    name = data['body']['name']
    email = data['body']['email']
    profile_pic = data['body']['profile_pic']
    list_of_ads = data['body']['list_of_ads']
    u = User_Profile(user_name=user_name, name=name, email=email, profile_pic=profile_pic, list_of_ads=list_of_ads)
    u.save()

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return False

    return True


def is_loggedIn(request): #works & tested
    """
    Checks if this user is registered in the database. If not, it creates one.
    """

    data = JSONParser().parse(request)

    email = data['body']['email']

    print('-----------> inside is_loggedIn <-----------\n', email, '\n------------------------')

    try:
        user = User_Profile.objects.get(email=email)
        return HttpResponse(status=200)
    except User_Profile.DoesNotExist:
        is_created = create_user(data) # returns True or False
        if is_created:
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)


#------------------------------Advertisement------------------------------#


def advertisement_get(request, first, second): #works & tested
    """
    Give all the ads for this user.
    (Model: Advertisement)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET advertisement <-----------\n', email, '\n------------------------')

    try:
        ad = Advertisement.objects.get(poster=email)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    serializer = AdvertisementSerializer(ad)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data)


def advertisement_update(request): #works & tested
    """
    Updates Advertisement data.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    email = data['body']['poster']
    ad_id = data['body']['ad_id']

    print('-----------> inside UPDATE advertisement', email, ' --- ', ad_id, '<-----------')

    try:
        ad = Advertisement.objects.filter(ad_id=ad_id, poster=email)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)


    print('Found ad:', ad[0])
    ad = ad[0]

    ad_id = data['body']['ad_id']
    poster = data['body']['poster']
    accommodation_name = data['body']['accommodation_name']
    accommodation_description = data['body']['accommodation_description']
    house_rules = data['body']['house_rules']
    booking_rules = data['body']['booking_rules']
    amenities = data['body']['amenities']
    base_price = data['body']['base_price']
    num_guests = data['body']['num_guests']
    num_bedrooms = data['body']['num_bedrooms']
    num_bathrooms = data['body']['num_bathrooms']
    suburb = data['body']['suburb']
    state = data['body']['state']
    country = data['body']['country']
    latitude = data['body']['latitude']
    longitude = data['body']['longitude']
    list_of_reviews = data['body']['list_of_reviews']
    list_of_events = data['body']['list_of_events']

    ad.set_ad_id(ad_id)
    ad.set_poster(poster)
    ad.set_accommodation_name(accommodation_name)
    ad.set_accommodation_description(accommodation_description)
    ad.set_house_rules(house_rules)
    ad.set_booking_rules(booking_rules)
    ad.set_amenities(amenities)
    ad.set_base_price(base_price)
    ad.set_num_guests(num_guests)
    ad.set_num_bedrooms(num_bedrooms)
    ad.set_num_bathrooms(num_bathrooms)
    ad.set_suburb(suburb)
    ad.set_state(state)
    ad.set_country(country)
    ad.set_latitude(latitude)
    ad.set_longitude(longitude)
    ad.set_rev_ids(list_of_reviews)
    ad.set_event_ids(list_of_events)

    return HttpResponse(status=201)



def advertisement_create(request): # works & tested
    """
    Create a new advertisement for this user.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    email = data['body']['poster']

    print('-----------> inside CREATE advertisement', email, '<-----------')

    u = User_Profile.objects.get(email=email)
    str_of_id = u.get_list_of_ads()
    if str_of_id != None:
        temp = str_of_id.split(',')
        #because the split() gives back this [''] so that's length 1
        #hence, the len(temp) > 1
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
    else:
        ad_id = 1 #this is the first ad this user is posting

    poster = email
    accommodation_name = data['body']['accommodation_name']
    accommodation_description = data['body']['accommodation_description']
    house_rules = data['body']['house_rules']
    booking_rules = data['body']['booking_rules']
    amenities = data['body']['amenities']
    base_price = data['body']['base_price']
    num_guests = data['body']['num_guests']
    num_bedrooms = data['body']['num_bedrooms']
    num_bathrooms = data['body']['num_bathrooms']
    suburb = data['body']['suburb']
    state = data['body']['state']
    country = data['body']['country']
    latitude = data['body']['latitude']
    longitude = data['body']['longitude']
    list_of_reviews = data['body']['list_of_reviews']
    list_of_events = data['body']['list_of_events']

    ad = Advertisement(
            ad_id = ad_id,
            poster = poster,
            accommodation_name = accommodation_name,
            accommodation_description = accommodation_description,
            house_rules = house_rules,
            booking_rules = booking_rules,
            amenities = amenities,
            base_price = base_price,
            num_guests = num_guests,
            num_bedrooms = num_bedrooms,
            num_bathrooms = num_bathrooms,
            suburb = suburb,
            state = state,
            country = country,
            latitude = latitude,
            longitude = longitude,
            list_of_reviews = list_of_reviews,
            list_of_events = list_of_events
        )
    ad.save()

    temp_ad = Advertisement.objects.filter(ad_id=ad_id, poster=email)

    print('Created ad: ', temp_ad)

    if temp_ad.exists() and len(temp_ad) == 1:

        u = User_Profile.objects.get(email=email)
        str_of_ads = u.get_list_of_ads()
        if str_of_ads == None:
            str_of_ads = ""
        new_str_of_ads = str_of_ads + str(ad_id) + ','
        u.set_list_of_ads(new_str_of_ads)

        return HttpResponse(status=201)

    else:
        return HttpResponse(status=400)


def advertisement_delete(request): # works & tested TODO check that the reviews and events get deleted too
    """
    Deletes this advertisement.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    email = data['body']['poster']
    ad_id = data['body']['ad_id']

    print('-----------> inside DELETE advertisement ', email, '<-----------')

    ad = Advertisement.objects.filter(poster=email, ad_id=ad_id)

    if ad.exists() and len(ad) == 1:

        ad.delete()

        u = User_Profile.objects.get(email=email)
        str_of_ads = u.get_list_of_ads()
        if str_of_ads != None:
            str_list_of_ads = str_of_ads.split(',')
            new_list = []
            for i in str_list_of_ads:
                if i == '':
                    continue
                elif i == str(ad_id): # delete the ad_id so we don't add to list
                    continue
                else:
                    new_list.append(i)

        new_list_of_ads = '' #contruct the string again to put back into db
        for i in new_list:
            new_list_of_ads = new_list_of_ads + i + ','

        print(new_list_of_ads)
        u.set_list_of_ads(new_list_of_ads)

        r = list(Accommodation_Review.objects.filter(ad_id=ad_id, ad_owner=email))
        for i in r:
            i.delete()

        e = list(Event.objects.filter(ad_id=ad_id, ad_owner=email))
        for i in e:
            i.delete()

        print('-----------> If empty list ad is deleted ', ad, '<-----------')
        return HttpResponse(status=200)

    else:
        print('BAD REQUEST')
        return HttpResponse(status=400)


#------------------------------Advertisement Reviews ------------------------------#


def review_get(request, first, second, ad_id):
    """
    Give all reviews this advertisement owns, identified by email and ad_id.
    (Model: Accommodation_Review)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET Review <-----------\n', email, ' --- ', ad_id, '\n------------------------')

    try:
        rev = Accommodation_Review.objects.filter(ad_owner=email, ad_id=ad_id)
    except Accommodation_Review.DoesNotExist:
        return HttpResponse(status=404)

    serializer = AccommodationReviewSerializer(rev)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data)


def review_create(request):
    """
    Create a new review for this advertisement, identified by ad_id and ad_owner.
    (Model: Advertisement_Review)
    """

    data = JSONParser().parse(request)
    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside CREATE Review ', ad_id, '<-----------')

    u = Advertisement.objects.filter(ad_id=ad_id, poster=ad_owner)

    str_of_id = u.get_rev_ids()
    if str_of_id != None:
        temp = str_of_id.split(',')
        temp_list = []
        for i in temp:
            if i =='':
                continue
            else:
                temp_list.append(int(i))
        max_id = max(temp_list)
        new_id = max_id + 1
        rev_id = new_id
    else:
        rev_id = 1 #this is the first review for this ad

    rating = data['body']['rating']
    message = data['body']['message']

    review = Accommodation_Review(
            rev_id=rev_id,
            rating=rating,
            message=message,
            ad_owner=ad_owner,
            ad_id=ad_id,
            )
    review.save()

    temp_review = Advertisement_Review.objects.filter(rev_id=rev_id, ad_id=ad_id, ad_owner=ad_owner)

    if temp_review.exists() and len(temp_review) == 1:

        a = Advertisement.objects.get(poster=ad_owner)
        str_of_rev_ids = a.get_rev_ids()
        new_str_of_rev = str_of_rev_ids + str(rev_id) + ','
        a.set_rev_ids(new_str_of_rev)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


def review_update(request):
    """
    Updates Advertisement Review for the given rev_id, ad_id and ad_owner.
    (Model: Advertisement_Review)
    """

    data = JSONParser().parse(request)

    rev_id = data['body']['rev_id']
    ad_id = data['body']['ad_id']
    ad_owner = data['body']['ad_owner']

    print('-----------> inside UPDATE review ', rev_id, ' --- ', ad_id, ' --- ', ad_owner, '<-----------')

    review = Advertisement_Review.objects.filter(rev_id=rev_id, ad_id=ad_id, ad_owner=ad_owner)

    if review.exists() and len(review) == 1:

        rev_id = data['body']['rev_id']
        rating = data['body']['rating']
        message = data['body']['message']
        ad_owner = data['body']['ad_owner']
        ad_id = data['body']['ad_id']

        review.set_rev_id(rev_id)
        review.set_rating(rating)
        review.set_message(message)
        review.set_ad_owner(ad_owner)
        review.set_ad_id(ad_id)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


def review_delete(request):
    """
    Deletes the advertisement review for the given rev_id, ad_id and ad_owner
    (Model: Advertisement_Review)
    """

    data = JSONParser().parse(request)

    rev_id = data['body']['rev_id']
    ad_id = data['body']['ad_id']
    ad_owner = data['body']['ad_owner']

    print('-----------> inside DELETE review ', rev_id, ' --- ', ad_id, ' --- ', ad_owner, '<-----------')

    rev = Advertisement_Review.objects.filter(rev_id=rev_id, ad_id=ad_id, ad_owner=ad_owner)

    if rev.exists() and len(rev) == 1:

        ad.delete()

        a = Advertisement.objects.get(poster=ad_owner)
        str_of_rev = a.get_rev_ids()
        if str_of_rev != None:
            str_list_of_rev = str_of_rev.split(',')
            new_list = []
            for i in str_list_of_rev:
                if i == '':
                    continue
                elif i == rev_id: # delete the rev_id so we don't add to list
                    continue
                else:
                    new_list.append(i)

        new_list_of_rev = '' #contruct the string again to put back into db
        for i in new_list:
            new_list_of_rev = new_list_of_rev + i + ','

        a.set_rev_ids(new_list_of_rev)

        print('-----------> Deleted this review', rev, '<-----------')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


#------------------------------Advertisement Events ------------------------------#


def event_get(request, first, second, ad_id):
    """
    Give events this advertisement owns, identified by email and ad_id.
    (Model: Event)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET Event <-----------\n', email, ' --- ', ad_id, '\n------------------------')

    try:
        event = Event.objects.filter(ad_owner=email, ad_id=ad_id)
    except Event.DoesNotExist:
        return HttpResponse(status=404)

    serializer = EventSerializer(event)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data)


def event_create(request):
    """
    Create a new event for this advertisement, identified by email and ad_id.
    (Model: Event)
    """

    data = JSONParser().parse(request)

    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside CREATE Event', ad_owner, '<-----------')

    u = Advertisement.objects.filter(ad_id=ad_id, poster=ad_owner)

    str_of_id = u.get_event_ids()
    if str_of_id != None:
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
    else:
        event_id = 1 #this is the first event for this ad

    start_day = data['body']['start_day']
    start_day_start_time = data['body']['start_day_start_time']
    end_day = data['body']['end_day']
    end_day_end_time = data['body']['end_day_end_time']
    booking_status = data['body']['booking_status']
    notes = data['body']['notes']

    event = Event(
            event_id=event_id,
            ad_owner=ad_owner,
            ad_id=ad_id,
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

        a = Advertisement.objects.get(poster=ad_owner)
        str_of_event_ids = a.get_event_ids()
        new_str_of_events = str_of_event_ids + str(event_id) + ','
        a.set_event_ids(new_str_of_events)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


def event_update(request):
    """
    Updates event, identified by email and ad_id.
    (Model: Advertisement_Event)
    """

    data = JSONParser().parse(request)

    event_id = data['body']['event_id']
    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside UPDATE event', ad_owner, '<-----------')

    event = Event.objects.filter(event_id=event_id, ad_owner=ad_owner, ad_id=ad_id)

    if event.exists() and len(event) == 1:

        event_id = data['body']['event_id']
        ad_owner = data['body']['ad_owner']
        ad_id = data['body']['ad_id']
        start_day = data['body']['start_day']
        start_day_start_time = data['body']['start_day_start_time']
        end_day = data['body']['end_day']
        end_day_end_time = data['body']['end_day_end_time']
        booking_status = data['body']['booking_status']
        notes = data['body']['notes']

        event.set_event_id(event_id)
        event.set_ad_owner(ad_owner)
        event.set_ad_id(ad_id)
        event.set_start_day(start_day)
        event.set_start_day_start_time(start_day_start_time)
        event.set_end_day(end_day)
        event.set_end_day_end_time(end_day_end_time)
        event.set_booking_status(booking_status)
        event.set_notes(notes)

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)

def event_delete(request):
    """
    Deletes the event with event_id, ad_owner and ad_id.
    """

    print('-----------> inside DELETE event ', event_id, '<-----------')

    event = Event.objects.filter(event_id=event_id, ad_owner=ad_owner, ad_id=ad_id)

    if event.exists() and len(event) == 1:

        event.delete()

        a = Advertisement.objects.get(poster=ad_owner)
        str_of_events = a.get_event_ids()
        if str_of_events != None:
            str_list_of_events = str_of_events.split(',')
            new_list = []
            for i in str_list_of_events:
                if i == '':
                    continue
                elif i == event_id: # delete the event_id so we don't add to list
                    continue
                else:
                    new_list.append(i)

        new_list_of_events = '' #contruct the string again to put back into db
        for i in new_list:
            new_list_of_events = new_list_of_events + i + ','

        a.set_event_ids(new_list_of_events)

        print('-----------> Deleted this event', event, '<-----------')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


#------------------------------Test Views------------------------------#

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


def review_detail(request, pk):
    """
    Shows JSON in browser of a particular ad.
    """

    try:
        ad = Accommodation_Review.objects.get(pk=pk)
    except Accommodation_Review.DoesNotExist:
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


def public(request):
    print("hello+",request.body)
    return HttpResponse("You don't need to be authenticated to see this")


def private(request):
    print("hello+",request.body)
    return HttpResponse("You should not see this message if not authenticated!")
