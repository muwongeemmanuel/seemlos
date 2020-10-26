from django.urls import path, include
from .views import index, line, numerical

app_name="analysis"
urlpatterns =[
    path('', index, name='analysis'),
    path('line-graph/', line, name="line" ),
    path('numerical/',numerical, name='numerical'),
]