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
def streams(request):
    streams = Stream.objects.all()
    serializer = StreamSerializer(streams, many=True)
    return Response(serializer.data)
