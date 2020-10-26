from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/')
def index(request):
    context={}
    return render(request, "index.html", context)

@login_required(login_url='/')
def numerical(request):
    context={}
    return render(request, "numerical.html", context)