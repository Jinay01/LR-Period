from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import *
from absuser.models import *

# older method
# class NewUser(UserCreationForm):
#     class Meta():
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


class UpdateStream(ModelForm):
    class Meta():
        model = College
        fields = ['stream']


class NewUser(UserCreationForm):
    class Meta():
        model = Collegeuser
        fields = ['email', 'username', 'password1', 'password2']
