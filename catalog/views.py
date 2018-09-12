from django.http import HttpResponse

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import Amenities, PropertyImage, Event
from catalog.models import User_Profile, User_Review

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import AmentitiesSerializer, PropertyImageSerializer, EventSerializer
from catalog.serializers import UserProfileSerializer, UserReviewSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# Advertisement model
@api_view(['GET', 'POST'])
def advertisement_list(request):
    """
    List all Advertisements, or create a new Advertisement.
    """
    if request.method == 'GET':
        ad = Advertisement.objects.all()
        serializer = AdvertisementSerializer(ad, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def advertisement_detail(request, pk):
    """
    Retrieve, update or delete an advertisement.
    """
    try:
        ad = Advertisement.objects.get(pk=pk)
    except ad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AdvertisementSerializer(ad)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        ad.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# ------------------------------------------------------------------------

def public(request):
    return HttpResponse("You don't need to be authenticated to see this")


@api_view(['GET'])
def private(request):
    return HttpResponse("You should not see this message if not authenticated!")
