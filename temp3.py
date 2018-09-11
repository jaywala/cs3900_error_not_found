@api_view(['GET', 'POST'])
def user_profile_list(request):
    """
    List all Advertisements, or create a new Advertisement.
    """
    if request.method == 'GET':
        temp = Advertisement.objects.all() # change
        serializer = AdvertisementSerializer(temp, many=True) #change
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AdvertisementSerializer(data=request.data) #change
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
