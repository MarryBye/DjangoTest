from django.contrib import admin
from django.urls import path
from apps.games.views import game_detail, game_list, game_form

urlpatterns = [
    path('', game_list, name='game_list'),
    path('game/<int:id>/', game_detail, name='game_detail'),
    path('game/new/', game_form, name='game_form')
]