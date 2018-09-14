
from django.http import *

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import PropertyImage, Event
from catalog.models import User_Profile, User_Review

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import PropertyImageSerializer, EventSerializer
from catalog.serializers import UserProfileSerializer, UserReviewSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import *

# Advertisement model
@csrf_exempt
@requires_csrf_token
def advertisement_list(request):
    """
    List all code snippets, or create a new snippet.
    """
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
@requires_csrf_token
def advertisement_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Advertisement.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'POST':
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
    return HttpResponse("You don't need to be authenticated to see this")

def private(request):
    return HttpResponse("You should not see this message if not authenticated!")
