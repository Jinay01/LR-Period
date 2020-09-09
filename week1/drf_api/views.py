from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


# Create your views here.


@api_view(['GET'])
def colleges(request):
    college = College.objects.all()
    context = CollegeSerializer(college, many=True)
    return Response(context.data)


@api_view(['GET'])
def collegeDetails(request, pk):
    college = College.objects.get(id=pk)
    college_details = CollegeSerializer(college, many=False)
    return Response(college_details.data)


@api_view(['GET'])
def streams(request):
    streams = Stream.objects.all()
    serializer = StreamSerializer(streams, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def streamNew(request):
    serializer_form = StreamSerializer(data=request.data)
    if serializer_form.is_valid():
        serializer_form.save()
    return Response(serializer_form.data)


@api_view(['POST', 'GET'])
def streamUpdate(request, pk):
    stream = Stream.objects.get(id=pk)
    serializer_form = StreamSerializer(instance=stream, data=request.data)
    if serializer_form.is_valid():
        serializer_form.save()
    return Response(serializer_form.data)


@api_view(['GET'])
def streamDelete(request, pk):
    stream = Stream.objects.get(id=pk)
    stream.delete()
    return Response('Stream deleted')
