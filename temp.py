# Amenities Model
@csrf_exempt
def Amenities_list(request):
    """
    List all Accommodation Review, or create a new Accommodation Review.
    """
    if request.method == 'GET':
        rev = Amenities.objects.all()
        serializer = AmentitiesSerializer(rev, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AmentitiesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def Amenities_detail(request, pk):
    """
    Retrieve, update or delete a Accommodation Review.
    """
    try:
        rev = Amenities.objects.get(pk=pk)
    except rev.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = AmentitiesSerializer(rev)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AmentitiesSerializer(rev, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        rev.delete()
        return HttpResponse(status=204)
