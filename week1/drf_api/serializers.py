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
