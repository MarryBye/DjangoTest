from django.contrib import admin
from apps.games.models import Game, Category, Image, Complexity

admin.site.register(Game)
admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Complexity)