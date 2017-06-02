from django.contrib.auth import authenticate, login, logout
from django.core import urlresolvers
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Person, Replacement


def show_login(request):
    return render(request, 'electronic/login.html')


def login_user(request):
    postdata = request.POST.copy()
    username = postdata.get("username", "")
    password = postdata.get("password", "")
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        url = urlresolvers.reverse('electronic:home')
        return HttpResponseRedirect(url)
    else:
        error_msg = "check your username and password!"
        return render(request, 'electronic/login.html', locals())


def registration_form(request):
    return render(request, 'electronic/registration_form.html')


def show_home(request):
    person = Person.objects.all()
    return render(request, 'electronic/home.html', {'person': person})
    # return render(request, 'electronic/home.html')


def logout_user(request):
    logout(request)
    url = urlresolvers.reverse('electronic:index')
    return HttpResponseRedirect(url)


def show_about(request):
    return render(request, 'electronic/about.html')


def new_id(request):
    return render(request, 'electronic/get_new_id.html')


def get_id_info(request):
    id_info = Person.objects.get(user = request.user)
    return render(request, 'electronic/replace_confirmation.html', {'id_info': id_info})


def do_replace(request):
    postdata = request.POST.copy()
    idno = postdata.get('idno', '')
    person = Person.objects.get(id_number=idno)
    phone_number = postdata.get('PhoneNumber')
    person.id_status = False
    replacement = Replacement()
    replacement.phone_number = phone_number
    replacement.first_name = person.first_name
    replacement.id_number = person
    replacement.save()
    return render(request, 'electronic/home.html')


def id_status(request):
    return render(request, 'electronic/id_status.html')


def get_queryset(request):
    person = Person.objects.all()
    return render(request, 'electronic/home.html', {'person': person})


def do_register(request):
    postdata = request.POST.copy()
    fname = postdata.get('fname', '')
    sname = postdata.get('sname', '')
    tname = postdata.get('tname', '')
    district_of_birth = postdata.get('district_of_birth', '')
    date_of_birth = postdata.get('date_of_birth', '')
    gender = postdata.get('gender', '')
    prev_person = Person.objects.latest('id_number')

    id_info = Person()
    id_info.first_name = fname
    id_info.second_name = sname
    id_info.third_name = tname
    id_info.district_of_birth = district_of_birth
    id_info.date_of_birth = date_of_birth
    id_info.gender = gender
    id_info.id_number = prev_person.id_number + 1
    print(request.user.username)

    id_info.user = request.user
    id_info.save()
    return render(request, 'electronic/get_new_id.html')


def account_register(request):
    postdata = request.POST.copy()
    username = postdata.get('username', '')
    email = postdata.get('email', '')
    password = postdata.get('password', '')
    newuser = User()
    newuser.username = username
    newuser.password = password
    newuser.email = email
    newuser.save()
    return render(request, 'electronic/login.html')
