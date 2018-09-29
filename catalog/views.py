
from django.http import *

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import Event, User_Profile

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import EventSerializer, UserProfileSerializer

from rest_framework.response import Response
from rest_framework.parsers import JSONParser


#------------------------------User_Profile------------------------------#


def user_profile_get(request, first, second):
    """
    Give all the information related to the user profile based on email.
    (Model: User_Profile).
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET user_profile <-----------\n', email, '\n------------------------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return HttpResponse(status=404)

    serializer = UserProfileSerializer(user)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data)



def user_profile_post(request, first, second):
    """
    Updates User Profile data for the given email.
    (Model: User_Profile)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside POST user_profile <-----------\n', email, '\n------------------------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return HttpResponse(status=404)

    data = JSONParser().parse(request)

    print('-----------> data to POST <-----------\n', data, '\n------------------------')

    user.set_user_name(data['body']['user_name'])
    current_user_name = user.get_user_name()

    user.set_name(data['body']['name'])
    current_name = user.get_name()

    print('name: ', current_name, '-----', data['body']['name'])
    print('user name: ', current_user_name, '-----', data['body']['user_name'])


    if data['body']['user_name'] != current_user_name or data['body']['name'] != current_name:
        print('MISTAKE')
        return HttpResponse(status=400)

    '''
    # can't let users update email because if they do our system
    # won't be able to find the same user.
    user.set_email(data['body']['email'])
    current_name = user.get_email()
    if data['body']['email'] != current_name:
        return HttpResponse(status=400)
    '''

    return HttpResponse(status=201)


def create_user(data):
    """
    Creates a new user profile.
    """

    user_name = data['body']['user_name']
    name = data['body']['name']
    email = data['body']['email']
    profile_pic = data['body']['profile_pic']
    u = User_Profile(user_name=user_name, name=name, email=email, profile_pic=profile_pic)
    u.save()
    return True


def is_loggedIn(request, first, second):
    """
    Checks if this user is registered in the database. If not, it creates one.
    """

    email = first + "@" + second + ".com"

    print('-----------> inside is_loggedIn <-----------\n', email, '\n------------------------')

    data = JSONParser().parse(request)
    email = data['body']['email']

    if data['body']['email'] != email:
        print('They should be the same as the person logged in should only \
               be changing thier user profile')

    user = User_Profile.objects.filter(email=email)

    if user.exists() and len(user) == 1:
        return HttpResponse(status=201)
    else:
        create_user(data)
        return HttpResponse(status=201)

    return HttpResponse(status=400)


#------------------------------Advertisement------------------------------#


def advertisement_get(request, first, second):
    """
    Give all the ads for this user.
    (models: Advertisement).
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET advertisement <-----------\n', email, '\n------------------------')

    try:
        ad = Advertisement.objects.filter(poster=email)
    except Advertisement.DoesNotExist:
        return HttpResponse(status=404)

    serializer = AdvertisementSerializer(ad)

    print('-----------> data given to frontend <-----------\n', serializer.data, '\n------------------------')

    return JsonResponse(serializer.data)


def advertisement_post(request, first, second, accommodation_name):
    """
    Updates Advertisement data for the given accommodation name.
    (Model: Advertisement)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside POST advertisement', email, '<-----------')

    ad = Advertisement.objects.filter(accommodation_name=accommodation_name)

    if ad.exists() and len(ad) == 1:
        data = JSONParser().parse(request)
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

        ad.set_poster(email)
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

        return HttpResponse(status=201)
    else:
        return HttpResponse(status=400)


def advertisement_create(request, first, second):
    """
    Create a new advertisement for this user.
    (Model: Advertisement)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside CREATE advertisement', email, '<-----------')

    data = JSONParser().parse(request)
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

    ad = Advertisement(poster = poster,
        accommodation_name = accommodation_name,
        accommodation_description = accommodation_description,
        house_rules = house_rules,
        base_price = base_price,
        num_guests = num_guests,
        num_bedrooms = num_bedrooms,
        num_bathrooms = num_bathrooms,
        latitude = latitude,
        longitude = longitude,
        suburb = suburb,
        amenities = amenities)
    ad.save()

    temp_ad = Advertisement.objects.filter(accommodation_name=accommodation_name)

    if temp_ad.exists() and len(temp_ad) == 1:
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=401)


def advertisement_delete(request, first, second, accommodation_name):
    """
    Deletes the ad with id number.
    """

    print('-----------> inside DELETE advertisement ', email, '<-----------')

    ad = Advertisement.objects.filter(accommodation_name=accommodation_name)

    if ad.exists() and len(ad) == 1:
        ad.delete()
        print('-----------> Deleted this ad ', ad, '<-----------')
        return HttpResponse(status=201)

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


def public(request):
    print("hello+",request.body)
    return HttpResponse("You don't need to be authenticated to see this")


def private(request):
    print("hello+",request.body)
    return HttpResponse("You should not see this message if not authenticated!")
