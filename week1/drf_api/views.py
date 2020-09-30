from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

# User registration using drf


@api_view(['POST'])
def registration_view(request):
    serializer = CollegeuserSerializer()
    if request.method == "POST":
        serializer = CollegeuserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            collegeuser = serializer.save()
            data['response'] = 'User is successfully created'
            data['email'] = collegeuser.email
            data['username'] = collegeuser.username
        else:
            data = serializer.error
        return Response(data)

# COLLEGE function bsed views


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
def collegeStreamDelete(request, pk, pk2):
    college = College.objects.get(id=pk)
    streams = college.stream_name.get(id=pk2)
    college.stream_name.remove(streams)
    return Response('Stream removed successfully')


@api_view(['GET', 'POST'])
# can only update college name not the streams
def collegeUpdate(request, pk):
    college = College.objects.get(id=pk)
    college_update = CollegeSerializer(
        instance=college, data=request.data, many=False)
    if college_update.is_valid():
        college_update.save()
    return Response(college_update.data)

# College classed based api views


class collegeApiView(APIView):
    def get(self, request):
        college = College.objects.all()
        college = CollegeSerializer(college, many=True)
        return Response(college.data)

    def post(self, request):
        serializer_data = CollegeSerializer(data=request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return Response(serializer_data.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class College1(APIView):

    def get_obj(self, pk):
        try:
            return College.objects.get(id=pk)
        except College.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        college = self.get_obj(pk)
        serializer = CollegeSerializer(college)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        college = self.get_obj(pk)
        serializer = CollegeSerializer(college, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, pk):
        college = self.get_obj(pk)
        college.delete()
        return Response('College deleted')


# STREAM
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


# METHOD 2 USING CLASS BASED VIEWS + HYPERLINK.....
# for students
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer2


# for stream
class StreamViewSet(viewsets.ModelViewSet):
    queryset = Stream.objects.all()
    serializer_class = StreamSerializer2


# for college


class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer2
