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
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
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
    college_id = pk
    # .name and .username will convert it to string
    # print(type(college))
    # print(type(user))
    context = {'college': college, 'user': user,
               'stream': stream, "college_id": college_id}
    return render(request, 'college/college_settings.html', context)


def stream_delete(request, pk, pk1):
    college = College.objects.get(id=pk)
    streams = college.stream.get(stream=pk1)
    # print(streams)
    if request.method == "POST":
        college.stream.remove(streams)
        return redirect('homePage')
    context = {'streams': streams}
    return render(request, 'college/stream_delete.html', context)


def update_stream(request, pk):
    college = College.objects.get(id=pk)
    form = UpdateStream(instance=college)
    if request.method == "POST":
        form = UpdateStream(request.POST, instance=college)
        if form.is_valid:
            form.save()
            return redirect('homePage')

    context = {'form': form, 'college': college}

    return render(request, 'college/update_stream.html', context)


def delete_college(request, pk):
    college = College.objects.get(id=pk)
    context = {'college': college}
    if request.method == 'POST':
        request.user.delete()
        college.delete()
        return redirect('homePage')
    return render(request, 'college/delete_college.html', context)


def logoutUser(request):
    logout(request)
    return redirect('loginpage')
