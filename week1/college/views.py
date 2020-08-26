from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .decoraters import unauthenticated_user
from django.contrib.auth.decorators import login_required

# Create your views here.


@unauthenticated_user
def regis(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save()
            college = form.cleaned_data.get('username')
            College.objects.create(
                name=college
            )
            return redirect('loginpage')

    context = {'form': form}
    return render(request, 'college/registration.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homePage')
        else:
            messages.info(request, "Username or Password is incorrect")

    context = {}
    return render(request, 'college/login.html', context)


@login_required(login_url='loginpage')
def homePage(request):
    college = College.objects.all()
    context = {'college': college}
    return render(request, 'college/home.html', context)


@login_required(login_url='loginpage')
def college_settings(request, pk):
    colleges = College.objects.get(id=pk)
    college = colleges.name
    user = request.user.username
    stream = colleges.stream.all()
    print(stream)
    # .name and .username will convert it to string
    # print(type(college))
    # print(type(user))
    context = {'college': college, 'user': user, 'stream': stream}
    return render(request, 'college/college_settings.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginpage')
