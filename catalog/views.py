from django.http import HttpResponse

from catalog.models import Advertisement, Accommodation_Review
from catalog.models import PropertyImage, Event
from catalog.models import User_Profile, User_Review

from catalog.serializers import AdvertisementSerializer, AccommodationReviewSerializer
from catalog.serializers import PropertyImageSerializer, EventSerializer
from catalog.serializers import UserProfileSerializer, UserReviewSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Advertisement model
@api_view(['GET', 'POST'])
def advertisement_list(request):
    """
    List all Advertisements, or create a new Advertisement.

    If it's a GET request, the function retrieves the page number from the GET
    request or use the first page by default if no page is submitted then retrieves
    the request page of ads, serialize it and return it back alongside with
    other information such as the next page and previous page links.

    If it's a POST request, the function creates the ad based on the POST data.
    """
    print("***inside ad list function")
    if request.method == 'GET':
        print('***inside GET_list')
        data = []
        nextPage = 1
        previousPage = 1
        ad = Advertisement.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(advertisement, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        serializer = AdvertisementSerializer(ad, context={'request: request'}, many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous:
            previous_page = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count,
        'numpages' : paginator.num_pages, 'nextlink': '/advertisement/?page=' + str(nextPage),
        'prevlink': '/advertisement/?page=' + str(previousPage)})

    elif request.method == 'POST':
        print('***inside POST')
        serializer = AdvertisementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def advertisement_detail(request, pk):
    """
    Retrieve, update or delete an advertisement.
    If it's a GET the ad is simply returned.
    If it's a PUT the ad is updated.
    If it's a DELETE the ad is deleted.
    """
    print("***inside ad detail function")
    try:
        ad = Advertisement.objects.get(pk=pk)
    except ad.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        print('***inside GET_detail')
        serializer = AdvertisementSerializer(ad, context={'request: request'})
        return Response(serializer.data)

    elif request.method == 'PUT':
        print('***inside PUT')
        serializer = AdvertisementSerializer(ad, data=request.data, context={'request: request'})
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
