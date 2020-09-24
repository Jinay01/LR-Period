from rest_framework import serializers
from college.models import *
from absuser.models import *

# Registration using drf


class CollegeuserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta():
        model = Collegeuser
        fields = ['email', 'username', 'password', 'password2']

    def save(self):
        collegeuser = Collegeuser(
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise Serializer.ValidationError(
                {'password': "Password doesnot match"})
        collegeuser.set_password(password)
        collegeuser.save()
        return collegeuser


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
