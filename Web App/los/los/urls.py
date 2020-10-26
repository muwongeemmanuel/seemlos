"""los URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index, base, register, contributors, user, signout, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home1/', home, name="home1" ),
    path('analysis/', include('analysis.urls')),
    path('web/', include('web_interface.urls')),
    path('', index, name="index" ),
    path('register/', register, name="register" ),
    path('base/',base, name="base" ),
    path('predict/', include('predict.urls')),
    path('contributors/', contributors, name="contributors" ),
    path('user-details/', user, name='user-details'),
    path('user-logout', signout, name='logout')
]



