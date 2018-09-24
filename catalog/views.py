
from django.http import *

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import PropertyImage, Event, User_Profile

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import PropertyImageSerializer, EventSerializer
from catalog.serializers import UserProfileSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import *


def user_profile(request, first, second):
    """
    Give all the information related to the user profile model.
    (models: User_Profile).
    """
    print('inside GET user_profile', first, second)

    snippets = Advertisement.objects.all()
    serializer = AdvertisementSerializer(snippets, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def user_profile_post(request, email):
    print("hello+",request.body)
    return HttpResponse("You don't need to be authenticated to see this")


# Advertisement model
@csrf_exempt
def advertisement_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    print("***inside ad list function")
    if request.method == 'GET':
        snippets = Advertisement.objects.all()
        serializer = AdvertisementSerializer(snippets, many=True)
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
