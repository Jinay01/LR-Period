from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewUser(UserCreationForm):
    class Meta():
        model = User
        # Doubt if fields mai if i am putting username even then i am getting fields for password
        fields = ['username', 'email', 'password1', 'password2']
