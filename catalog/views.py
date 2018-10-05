
from django.http import *

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import Event, User_Profile

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import EventSerializer, UserProfileSerializer

from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.db.models import Max


#------------------------------User_Profile------------------------------#

def user_profile_get(request, first, second):
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


def user_profile_update(request):
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

    new_user_name = data['body']['given_name']
    new_name = data['body']['name']
    new_email = data['body']['email']
    new_profile_pic = data['body']['picture']
    #new_list_of_ads = data['body']['list_of_ads']
    #new_list_of_rentals = data['body']['list_of_rentals']
    #new_list_of_posted_reviews = data['body']['list_of_posted_reviews']


    user.set_user_name(new_user_name)
    user.set_name(new_name)
    user.set_email(new_email)
    user.set_profile_pic(new_profile_pic)
    #user.set_list_of_ads(new_list_of_ads)
    #user.set_list_of_rentals(new_list_of_rentals)
    #user.set_list_of_posted_reviews(new_list_of_posted_reviews)

    return HttpResponse(status=200)


def create_user(data):
    """
    Creates a new user profile.
    """

    user_name = data['body']['given_name']
    name = data['body']['name']
    email = data['body']['email']
    profile_pic = data['body']['picture']
    list_of_ads = "" #data['body']['list_of_ads']
    list_of_rentals = "" #data['body']['list_of_rentals']
    list_of_posted_reviews = "" #data['body']['list_of_posted_reviews']

    u = User_Profile(user_name=user_name,
                     name=name,
                     email=email,
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

    return True


def is_loggedIn(request):
    """
    Checks if this user is registered in the database. If not, it creates one.
    """

    data = JSONParser().parse(request)
    email = data['body']['email']

    print('-----------> inside is_loggedIn <-----------\n', email, '\n------------------------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        is_created = create_user(data) # returns True or False
        if is_created:
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)

    return HttpResponse(status=200)


#------------------------------Advertisement------------------------------#

def advertisement_get(request, first, second):
    """
    Give all the ads for this user.
    (Model: Advertisement)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET advertisement <-----------\n', email, '\n------------------------')

    try:
        ad = Advertisement.objects.filter(poster=email)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    serializer = AdvertisementSerializer(ad, many=True)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data, safe=False)


def advertisement_update(request):
    """
    Updates Advertisement data.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    email = data['body']['poster']
    ad_id = data['body']['ad_id']

    print('-----------> inside UPDATE advertisement <-----------\n', email, ' --- ', ad_id, '\n------------------------')

    try:
        ad = Advertisement.objects.filter(ad_id=ad_id, poster=email)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)


    print('Found ad:', ad[0])
    ad = ad[0]

    ad_id = data['body']['ad_id']
    poster = data['body']['poster']
    accommodation_name = data['body']['title']
    accommodation_description = data['body']['summary']
    house_rules = "" #data['body']['house_rules']
    booking_rules = "" #data['body']['booking_rules']
    amenities = data['body']['amenities']
    base_price = 50 #data['body']['base_price']
    num_guests = data['body']['nGuests']
    num_bedrooms = data['body']['nBedrooms']
    num_bathrooms = data['body']['nBathrooms']
    address = data['body']['address']
    zip_code = data['body']['zipCode']
    cit = data['body']['city']
    latitude = 0 #data['body']['latitude'] # TODO function to fill this in
    longitude = 0 #data['body']['longitude']
    property_type = data['body']['propertyType']

    # because we are updating, we don't need to change these
    #list_of_reviews = data['body']['list_of_reviews']
    #list_of_events = data['body']['list_of_events']
    #list_of_images = data['body']['list_of_images']

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
    ad.set_address(address)
    ad.zip_code(zip_code)
    ad.city(city)
    ad.set_latitude(latitude)
    ad.set_longitude(longitude)
    ad.set_property_type(property_type)
    #ad.set_rev_ids(list_of_reviews)
    #ad.set_event_ids(list_of_events)
    #ad.set_image_ids(list_of_images)

    return HttpResponse(status=201)


def advertisement_create(request):
    """
    Create a new advertisement for this user.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    email = data['body']['poster']

    print('-----------> inside CREATE advertisement <-----------\n', email, '\n------------------------')

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
    accommodation_name = data['body']['title']
    accommodation_description = data['body']['summary']
    house_rules = "" #data['body']['house_rules']
    booking_rules = "" #data['body']['booking_rules']
    amenities = data['body']['amenities']
    base_price = 50 #data['body']['base_price']
    num_guests = data['body']['nGuests']
    num_bedrooms = data['body']['nBedrooms']
    num_bathrooms = data['body']['nBathrooms']
    address = data['body']['address']
    city = "Sydney"
    zip_code = data['body']['zipCode']
    latitude = 0 #data['body']['latitude']
    longitude = 0 #data['body']['longitude']
    list_of_reviews = "" #data['body']['list_of_reviews']
    list_of_events = "" #data['body']['list_of_events']
    list_of_images = ""
    property_type = data['body']['propertyType']

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
            address = address,
            city = city,
            zip_code = zip_code,
            latitude = latitude,
            longitude = longitude,
            list_of_reviews = list_of_reviews,
            list_of_events = list_of_events,
            property_type = propertyType,
            list_of_images = list_of_images,
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


def advertisement_delete(request):
    """
    Deletes this advertisement.
    (Model: Advertisement)
    """

    data = JSONParser().parse(request)

    email = data['body']['poster']
    ad_id = data['body']['ad_id']

    print('-----------> inside DELETE advertisement <-----------\n', email, '\n------------------------')

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

        u.set_list_of_ads(new_list_of_ads)

        r = list(Accommodation_Review.objects.filter(ad_id=ad_id, ad_owner=email))
        for j in r:
            j.delete()

        e = list(Event.objects.filter(ad_id=ad_id, ad_owner=email))
        for j in e:
            j.delete()

        i = list(PropertyImage.objects.filter(ad_owner=ad_owner, ad_id=ad_id))
        for j in i:
            j.delete()

        print('-----------> If empty list ad is deleted <-----------\n', ad, '\n------------------------')
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

    serializer = AccommodationReviewSerializer(rev, many=True)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data, safe=False)


def review_create(request):
    """
    Create a new review for this advertisement, identified by ad_id and ad_owner.
    (Model: Advertisement_Review)
    """

    data = JSONParser().parse(request)
    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside CREATE Review <-----------\n', ad_id, '\n------------------------')

    u = Advertisement.objects.filter(ad_id=ad_id, poster=ad_owner)
    str_of_id = u[0].get_rev_ids()
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

    temp_review = Accommodation_Review.objects.filter(rev_id=rev_id, ad_id=ad_id, ad_owner=ad_owner)

    if temp_review.exists() and len(temp_review) == 1:

        a = Advertisement.objects.get(poster=ad_owner, ad_id=ad_id)
        str_of_rev_ids = a.get_rev_ids()
        if str_of_rev_ids == None:
            new_str_of_rev = str(rev_id) + ',' # first review for this ad
        else:
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

    print('-----------> inside UPDATE review <-----------\n', rev_id, ' --- ', ad_id, ' --- ', ad_owner, '\n------------------------')

    review = Accommodation_Review.objects.filter(rev_id=rev_id, ad_id=ad_id, ad_owner=ad_owner)
    review = review[0]

    #if review.exists() and len(review) == 1:
    #NOTE: not sure why sometimes .exists() works for model instances and sometimes it doesn't
    #TODO look into this later

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
    #else:
    #    return HttpResponse(status=400)


def review_delete(request):
    """
    Deletes the advertisement review for the given rev_id, ad_id and ad_owner
    (Model: Advertisement_Review)
    """

    data = JSONParser().parse(request)

    rev_id = data['body']['rev_id']
    ad_id = data['body']['ad_id']
    ad_owner = data['body']['ad_owner']

    print('-----------> inside DELETE review <-----------\n', rev_id, ' --- ', ad_id, ' --- ', ad_owner, '\n------------------------')

    rev = Accommodation_Review.objects.filter(rev_id=rev_id, ad_id=ad_id, ad_owner=ad_owner)

    if rev.exists() and len(rev) == 1:

        rev.delete()

        a = Advertisement.objects.filter(poster=ad_owner, ad_id=ad_id)
        a = a[0]
        str_of_rev = a.get_rev_ids()
        if str_of_rev != None:
            str_list_of_rev = str_of_rev.split(',')
            new_list = []
            for i in str_list_of_rev:
                if i == '':
                    continue
                elif i == str(rev_id): # delete the rev_id so we don't add to list
                    continue
                else:
                    new_list.append(i)

        new_list_of_rev = '' #contruct the string again to put back into db
        for i in new_list:
            new_list_of_rev = new_list_of_rev + i + ','

        a.set_rev_ids(new_list_of_rev)

        print('-----------> If deleted this should be empty ', rev, '\n------------------------')
        return HttpResponse(status=200)
    else:
        print('BAD REQUEST')
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

    serializer = EventSerializer(event, many=True)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data, safe=False)


def event_create(request):
    """
    Create a new event for this advertisement, identified by email and ad_id.
    (Model: Event)
    """

    data = JSONParser().parse(request)

    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside CREATE Event <-----------\n', ad_owner, '\n------------------------')

    u = Advertisement.objects.get(ad_id=ad_id, poster=ad_owner)

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

        a = Advertisement.objects.get(ad_id=ad_id, poster=ad_owner)
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

    print('-----------> inside UPDATE event <-----------\n', ad_owner, '\n------------------------')

    event = Event.objects.filter(event_id=event_id, ad_owner=ad_owner, ad_id=ad_id)

    if event.exists() and len(event) == 1:

        event = event[0]

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

    data = JSONParser().parse(request)

    event_id = data['body']['event_id']
    ad_owner = data['body']['ad_owner']
    ad_id = data['body']['ad_id']

    print('-----------> inside DELETE event <-----------\n', event_id, '\n------------------------')

    event = Event.objects.filter(event_id=event_id, ad_owner=ad_owner, ad_id=ad_id)

    if event.exists() and len(event) == 1:

        event.delete()

        a = Advertisement.objects.get(poster=ad_owner, ad_id=ad_id)
        str_of_events = a.get_event_ids()
        if str_of_events != None:
            str_list_of_events = str_of_events.split(',')
            new_list = []
            for i in str_list_of_events:
                if i == '':
                    continue
                elif i == str(event_id): # delete the event_id so we don't add to list
                    continue
                else:
                    new_list.append(i)

        new_list_of_events = '' #contruct the string again to put back into db
        for i in new_list:
            new_list_of_events = new_list_of_events + i + ','

        a.set_event_ids(new_list_of_events)

        print('-----------> If deleted this is an empty list ', event, '\n------------------------')
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)


#------------------------------ General Views ------------------------------#

def get_single_ad(request, first, second, ad_id):
    """
    Gives ONE ad, identified by email and ad_id.
    (Model: Advertisement)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET SINGLE advertisement <-----------\n', email, '\n------------------------')

    try:
        ad = Advertisement.objects.get(poster=email, ad_id=ad_id)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    serializer = AdvertisementSerializer(ad)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data)


def get_all_ads(request):
    """
    Gets all the ads in the db.
    (Model: Advertisement)
    """

    print('-----------> inside get_all_ads <-----------')

    try:
        a = Advertisement.objects.all()
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    serializer = AdvertisementSerializer(a, many=True)

    #print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data, safe=False)


#------------------------------Search Module Views------------------------------#




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


def public(request):
    print("hello+",request.body)
    return HttpResponse("You don't need to be authenticated to see this")


def private(request):
    print("hello+",request.body)
    return HttpResponse("You should not see this message if not authenticated!")
