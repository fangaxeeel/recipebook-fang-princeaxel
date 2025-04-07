from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeImageForm, RecipeForm, RecipeIngredientForm

@login_required
def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, "recipe_list.html", {"recipes": recipes})

@login_required
def recipe_detail(request, num):
    recipe = Recipe.objects.get(id=num)
    return render(request, "recipe_detail.html", {"recipe": recipe})

@login_required
def add_image(request, num):
    try:
        recipe = Recipe.objects.get(pk=num)
    except Recipe.DoesNotExist:
        return redirect('recipe_list')

    if request.method == 'POST':
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('recipe_detail', num=recipe.pk)
    else:
        form = RecipeImageForm()

    return render(request, 'add_image.html', {'form': form, 'recipe': recipe})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        recipe_form = RecipeForm(request.POST)
        ingredient_form = RecipeIngredientForm(request.POST)

        if recipe_form.is_valid() and ingredient_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            ingredient = ingredient_form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()

            return redirect('recipe_detail', num=recipe.pk)
    else:
        recipe_form = RecipeForm()
        ingredient_form = RecipeIngredientForm()

    return render(request, 'add_recipe.html', {
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
    })