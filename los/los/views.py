from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required


def home(request):
    context={}
    return render(request, "index/home.html", context)

def index(request):
    if not request.user.is_authenticated:
        if request.method=="POST":
            username = request.POST.get('uname')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                context={'alert':"Failed to login. Retry or contact the system admin..."}
                return render(request, "index/index.html", context)
            else:
                login(request, user)
                return HttpResponseRedirect('/home1')
    else:
        return HttpResponseRedirect('/home1')
    context={}
    return render(request, "index/index.html", context)

def register(request):
    if request.method=="POST":
        username = request.POST.get('uname')
        email = request.POST.get('email')
        position = request.POST.get('position')
        password = request.POST.get('password')
        g = Group.objects.get(name=position)
        user = User.objects.create_user(username, email, password)
        g.user_set.add(user)
        login(request, username)
        return HttpResponseRedirect('/')
    context={}
    return render(request, "index/register.html", context)


def base(request):
    context={}
    return render(request, 'base/base1.html', context)

@login_required(login_url='/')
def contributors(request):
    context={}
    return render(request, 'index/contributors.html', context)

@login_required(login_url='/')
def user(request):
    context={}
    return render(request, 'index/user.html', context)

@login_required(login_url='/')
def signout(request):
    logout(request)
    context={}
    return HttpResponseRedirect('/')