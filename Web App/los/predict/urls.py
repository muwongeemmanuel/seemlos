from django.urls import path
from .views import index, numerical

app_name="predict"
urlpatterns =[
    path('', index, name="predict-graphs"),
    path("numerical/", numerical, name='predict-num'),
]