from django import forms
from apps.games.models import Game, Category, Complexity

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['name', 'description', 'category', 'complexity', 'logo']
        
class FilterForm(forms.Form):
    search = forms.CharField(required=False, label='Search')
    category = forms.ModelChoiceField(Category.objects, required=False)
    complexity = forms.ModelChoiceField(Complexity.objects, required=False)