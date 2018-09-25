
from django.http import *

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import PropertyImage, Event, User_Profile

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import PropertyImageSerializer, EventSerializer
from catalog.serializers import UserProfileSerializer

from rest_framework.response import Response
from rest_framework.parsers import JSONParser


def user_profile_get(request, first, second):
    """
    Give all the information related to the user profile based on email.
    (Model: User_Profile).
    """

    email = first + "@" + second + ".com"

    print('-----------> inside GET user_profile', email, '<-----------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return HttpResponse(status=404)

    serializer = UserProfileSerializer(user)

    print('-----------> data given to frontend ', serializer.data, '<-----------')

    return JsonResponse(serializer.data)


def user_profile_post(request, first, second):
    """
    Updates User Profile data for the given email.
    (Model: User_Profile)
    """

    email = first + "@" + second + ".com"

    print('-----------> inside POST user_profile', email, '<-----------')

    try:
        user = User_Profile.objects.get(email=email)
    except User_Profile.DoesNotExist:
        return HttpResponse(status=404)

    data = JSONParser().parse(request)

    print('data', data)
    print('***', data['body']['user_name'], '***')

    user.set_user_name(data['body']['user_name'])
    current_name = user.get_user_name()
    print(current_name)
    if data['body']['user_name'] != current_name:
        return HttpResponse("did not change user name")

    return HttpResponse("worked")
    '''
    serializer = UserProfileSerializer(user, data=data)
    if serializer.is_valid():
        serializer.save()
        print('SAVED')
        return JsonResponse(serializer.data, status=201)
    print('serializer', serializer)
    return JsonResponse(serializer.errors)#, status=400)
    '''

def advertisement_get(request, first, second):
    """
    Give all the ads for this user.
    (models: Advertisement).
    """

    print('-----------> inside GET advertisement', email, '<-----------')

    snippets = Advertisement.objects.all()
    serializer = AdvertisementSerializer(snippets, many=True)

    print('-----------> data given to frontend ', serializer.data, '<-----------')

    return JsonResponse(serializer.data)


def advertisement_post(request, first, second, user):
    print("hello+",request.body)

    data = JSONParser().parse(request)
    serializer = AdvertisementSerializer(data=data)

    print('info======' , serializer)
    print('isSaved', serializer.is_valid())

    if serializer.is_valid():
        serializer.save()
        print('SAVED')
        return HttpResponse("saved")#JsonResponse(serializer.data, status=201)
    return HttpResponse("invalid data")
    #return JsonResponse(serializer.errors, status=400)


def advertisement_detail(request, pk):
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
