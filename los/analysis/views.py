from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/')
def index(request):
    context={}
    return render(request, "analysis/index.html", context)

@login_required(login_url='/')
def line(request):
    context={}
    return render(request, "analysis/line.html", context)

@login_required(login_url='/')
def numerical(request):
    context={}
    return render(request, "analysis/numerical.html", context)

