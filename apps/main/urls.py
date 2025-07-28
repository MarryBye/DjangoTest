from django.contrib import admin
from django.urls import path
from apps.main.views import home

urlpatterns = [
    path('', home, name='home_page')
]