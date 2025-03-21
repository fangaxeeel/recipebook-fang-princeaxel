from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recipe

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, num):
    recipe = Recipe.objects.get(id=num)
    return render(request, "recipe_detail.html", {"recipe": recipe})