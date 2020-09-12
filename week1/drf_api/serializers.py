from rest_framework import serializers
from college.models import *


class StreamSerializer(serializers.ModelSerializer):
    class Meta():
        model = Stream
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    # this is done so that we can get both id as well as stream name or else we will only get id of that stream
    stream_name = StreamSerializer(read_only=True, many=True)

    class Meta():
        model = College
        fields = ['id', 'college_name', 'stream_name']


# if we want stream in college then we need to first add streams serializer

# stream method 2
class StreamSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Stream
        fields = '__all__'

# student


class StudentSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = Student
        fields = '__all__'


# college method 2
class CollegeSerializer2(serializers.HyperlinkedModelSerializer):
    class Meta():
        model = College
        fields = '__all__'
