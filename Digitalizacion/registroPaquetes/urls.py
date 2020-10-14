from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='registroPaquetes'),
    path('verificaDatos/', views.verificaDatos, name='verificaDatos')
]
