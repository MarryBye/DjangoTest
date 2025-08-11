from django.contrib import admin
from django.urls import path
from apps.games.views import GameListView

urlpatterns = [
    path('', GameListView.as_view(), name='game_list')
]