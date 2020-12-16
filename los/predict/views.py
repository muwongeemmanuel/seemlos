from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import requests


# Create your views here.
@login_required(login_url='/')
def index(request):
    if request.method == "POST":
        weeks = request.POST.get('weeks')
        r = requests.post('http://127.0.0.1:5000/weeklyforecast', json={"Weeks":str(weeks)})
        rounded_labour=list()
        forecast=r.json()
        for total in forecast:
            for number in total:
                labour= float(number)
                show_digit = round(labour)
                rounded_labour.append(show_digit)
                
        return render(request, "index.html", {'forecast':rounded_labour})
    r = requests.post('http://127.0.0.1:5000/weeklyforecast', json={"Weeks":"4"})
    rounded_labour=list()
    forecast=r.json()
    for total in forecast:
        for number in total:
            labour= float(number)
            show_digit = round(labour)
            rounded_labour.append(show_digit)
            
    return render(request, "index.html", {'forecast':rounded_labour})

@login_required(login_url='/')
def numerical(request):
    #response = requests.get('http://127.0.0.1:5000/dailyforecast').json()
    if request.method == "POST":
        days = request.POST.get('days')
        r = requests.post('http://127.0.0.1:5000/multidailyforecast', json={"Days":str(days)})
        rounded_labour=list()
        forecast=r.json()
        print(forecast)
        for total in forecast:
            for number in total:
                labour= int(number)
                show_digit = round(labour)
                rounded_labour.append(show_digit)
        return render(request, "numerical.html", {"forecast":rounded_labour})
    r = requests.post('http://127.0.0.1:5000/multidailyforecast', json={"Days":"7"})
    rounded_labour=list()
    forecast=r.json()
    print(forecast)
    for total in forecast:
        for number in total:
            labour= int(number)
            show_digit = round(labour)
            rounded_labour.append(show_digit)
    return render(request, "numerical.html", {"forecast":rounded_labour})
    #return render(request, "numerical.html", {"forecast":rounded_labour})

@login_required(login_url='/')
def monthly(request):
    r = requests.post('http://127.0.0.1:5000/monthlyforecast', json={"Months":"3"})
    rounded_labour=list()
    show_data = dict()
    forecast=r.json()
    for total in forecast:
        for number in total:
            labour= float(number)
            show_digit = round(labour)
            #rounded_labour.append(show_digit)
            show_data={
                "show":labour,
                "real":show_digit
            }
            rounded_labour.append(show_data)
            
    return render(request, "month.html", {'forecast':rounded_labour, 'show_data':show_data})