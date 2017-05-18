from django.contrib.auth import authenticate, login, logout
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from django.shortcuts import render


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
    return render(request, 'electronic/home.html')

def logout_user(request):
    logout(request)
    url = urlresolvers.reverse('electronic:index')
    return HttpResponseRedirect(url)