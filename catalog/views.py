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
from catalog.models import Advertisement
from catalog.serializers import AdvertisementSerializer

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
    except ad.DoesNotExist:
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
        ad.delete()
        return HttpResponse(status=204)



# ******END******

def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")

def index(request):
    return HttpResponse("Home Page")
