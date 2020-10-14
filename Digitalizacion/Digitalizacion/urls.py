"""Digitalizacion URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls import url
from django.views.generic import TemplateView
from Digitalizacion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('verificacion', views.verificacion)
]

"""
path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('genPassword/', include('genPassword.urls')),
    path('cesar/', include('cesar.urls')),
    path('transposicion/', include('transposicion.urls')),
    path('portada/', include('portada.urls')),


"""