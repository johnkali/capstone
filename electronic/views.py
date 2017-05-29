from django.contrib.auth import authenticate, login, logout
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View

from .models import Person
from .forms import UserForm

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


def show_home(request):
    person = Person.objects.all()
    return render(request, 'electronic/home.html', {'person': person})
    #return render(request, 'electronic/home.html')


def logout_user(request):
    logout(request)
    url = urlresolvers.reverse('electronic:index')
    return HttpResponseRedirect(url)


def show_about(request):
    return render(request, 'electronic/about.html')


def new_id(request):
    return render(request, 'electronic/get_new_id.html')


def replace_id(request):
    return render(request, 'electronic/replace_id.html')

def id_status(request):
    return render(request, 'electronic/id_status.html')

def get_queryset(request):
    person = Person.objects.all()
    return render(request, 'electronic/home.html', {'person': person})
class UserFormView(View):
    form_class = UserForm
    template_name = 'electronic/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            url = urlresolvers.reverse('electronic:home')
            return HttpResponseRedirect(url)

