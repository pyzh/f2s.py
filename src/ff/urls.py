from django.urls import path

from . import views

urlpatterns = [
    path('', views.目录, name='index'),
]