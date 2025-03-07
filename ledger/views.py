from django.shortcuts import render
from .models import Recipe

def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail(request, num):
    recipe = Recipe.objects.get(id=num)
    return render(request, 'recipe_detail.html', {'recipe': recipe})
