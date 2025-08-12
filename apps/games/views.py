from django.shortcuts import render, redirect
from django.core import paginator

from django.views.generic import ListView, DetailView
from apps.games.models import Game
from apps.games.forms import GameForm, FilterForm

def game_list(request):
    
    filters_form = FilterForm(request.GET or None)
    filters = {}
    
    for field in filters_form.changed_data:
        if field == 'search':
            filters['name__icontains'] = request.GET.get('search')
            continue
        filters[field] = request.GET.get(field)

    games = Game.objects.filter(**filters)
    
    pages = paginator.Paginator(games, 10)
    page_number = request.GET.get('page')
    page_obj = pages.get_page(page_number)
    
    return render(request, 'games/game_list.html', {'page_obj': page_obj, 'filters_form': filters_form})

def game_detail(request, id):
    game = Game.objects.get(id=id)
    return render(request, 'games/game_detail.html', {'game': game})

def game_form(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)
        if form.is_valid():
            game = form.save()
            return redirect('game_detail', id=game.id)
    else:
        form = GameForm()
    return render(request, 'games/game_form.html', {'form': form})
