
from django.http import *

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import PropertyImage, Event, User_Profile

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import PropertyImageSerializer, EventSerializer
from catalog.serializers import UserProfileSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import *


def user_profile_get(request, first, second):
    """
    Give all the information related to the user profile based on email.
    (model: User_Profile).
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


def user_profile_post(request, first, second, user):
    return HttpResponse(status=204)


def advertisement_get(request, first, second):
    """
    Give all the ads for this user.
    (models: Advertisement).
    """

    print('-----------> inside GET advertisement', first, second, 'contrusted email: ', email, '<-----------')

    snippets = Advertisement.objects.all()
    serializer = AdvertisementSerializer(snippets, many=True)
    print("data given back to frontend =========>", serializer.data)
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
    """
    Retrieve, update or delete a code snippet.
    """
    print("***inside ad detail function")
    print('here', request.GET.get("accommodation_name", ""))
    try:
        snippet = Advertisement.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
        print('inside POST********************')
        data = JSONParser().parse(request)
        serializer = AdvertisementSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
    else:
        return HttpResponse(status=404)

def public(request):
    print("hello+",request.body)
    return HttpResponse("You don't need to be authenticated to see this")

def private(request):
    print("hello+",request.body)
    return HttpResponse("You should not see this message if not authenticated!")
