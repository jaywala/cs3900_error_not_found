from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from django.http import HttpResponse

# writing Django views using Serializer
# *****START*****
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from catalog.models import Advertisement, Accommodation_Review, Amenities, PropertyImage, Event
from catalog.models import User_Profile, User_Review
from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import AmentitiesSerializer, PropertyImageSerializer, EventSerializer
from catalog.serializers import UserProfileSerializer, UserReviewSerializer

# Advertisement model
@csrf_exempt
def advertisement_list(request):
    """
    List all advertisements, or create a new advertisement.

    Note that because we want to be able to POST to this view from clients
    that won't have a CSRF token we need to mark the view as csrf_exempt.
    This isn't something that you'd normally want to do, and REST framework
    views actually use more sensible behavior than this, but it'll do for our
    purposes right now.
    """
    if request.method == 'GET':
        ads = Advertisement.objects.all()
        serializer = AdvertisementSerializer(ads, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdvertisementSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def advertisement_detail(request, pk):
    """
    Retrieve, update or delete a Advertisement.
    """
    try:
        ad = Advertisement.objects.get(pk=pk)
    except ad.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(ad)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AdvertisementSerializer(ad, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        ad.delete()
        return HttpResponse(status=204)


# User_Profile Model
@csrf_exempt
def user_profile_list(request):
    """
    List all User Profiles, or create a new User Profile.
    """
    if request.method == 'GET':
        users = User_Profile.objects.all()
        serializer = UserProfileSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_profile_detail(request, pk):
    """
    Retrieve, update or delete a User Profile.
    """
    try:
        user = User_Profile.objects.get(pk=pk)
    except user.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserProfileSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


# User_Review Model
@csrf_exempt
def user_review_list(request):
    """
    List all User Reviews, or create a new User Review.
    """
    if request.method == 'GET':
        rev = User_Review.objects.all()
        serializer = UserReviewSerializer(rev, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_review_detail(request, pk):
    """
    Retrieve, update or delete a User Review.
    """
    try:
        rev = User_Review.objects.get(pk=pk)
    except rev.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserReviewSerializer(rev)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserReviewSerializer(rev, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rev.delete()
        return HttpResponse(status=204)


# Accommodation_Review Model
@csrf_exempt
def accommodation_review_list(request):
    """
    List all Accommodation Review, or create a new Accommodation Review.
    """
    if request.method == 'GET':
        rev = Accommodation_Review.objects.all()
        serializer = AccommodationReviewSerializer(rev, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AccommodationReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def accommodation_review_detail(request, pk):
    """
    Retrieve, update or delete a Accommodation Review.
    """
    try:
        rev = Accommodation_Review.objects.get(pk=pk)
    except rev.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AccommodationReviewSerializer(rev)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AccommodationReviewSerializer(rev, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rev.delete()
        return HttpResponse(status=204)


# Amenities Model
@csrf_exempt
def amenities_list(request):
    """
    List all Amenties, or create a new Amenity.
    """
    if request.method == 'GET':
        am = Amenities.objects.all()
        serializer = AmentitiesSerializer(am, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AmentitiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def amenities_detail(request, pk):
    """
    Retrieve, update or delete an Amenity.
    """
    try:
        am = Amenities.objects.get(pk=pk)
    except am.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AmentitiesSerializer(am)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AmentitiesSerializer(am, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        am.delete()
        return HttpResponse(status=204)


# PropertyImage Model
@csrf_exempt
def property_image_list(request):
    """
    List all PropertyImage, or create a new PropertyImage.
    """
    if request.method == 'GET':
        im = PropertyImage.objects.all()
        serializer = PropertyImageSerializer(im, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PropertyImageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def property_image_detail(request, pk):
    """
    Retrieve, update or delete an PropertyImage.
    """
    try:
        im = PropertyImage.objects.get(pk=pk)
    except im.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PropertyImageSerializer(im)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PropertyImageSerializer(im, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        im.delete()
        return HttpResponse(status=204)


# Event Model
@csrf_exempt
def event_list(request):
    """
    List all Events, or create a new Event.
    """
    if request.method == 'GET':
        event = Event.objects.all()
        serializer = EventSerializer(event, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def event_detail(request, pk):
    """
    Retrieve, update or delete an Event.
    """
    try:
        event = Event.objects.get(pk=pk)
    except event.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = EventSerializer(event, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        event.delete()
        return HttpResponse(status=204)

# ******END******

def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")

def index(request):
    return HttpResponse("Home Page")
