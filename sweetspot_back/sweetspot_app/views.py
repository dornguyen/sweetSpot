from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Spot
from .serializers import SpotSerializer

@api_view(['GET', 'POST'])
def spot_list(request):
    if request.method == 'GET':
        spots = Spot.objects.all()
        serializer = SpotSerializer(spots, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SpotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def spot_detail(request, pk):
    try:
        spot = Spot.objects.get(pk=pk)
    except Spot.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SpotSerializer(spot)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SpotSerializer(spot, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        spot.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)