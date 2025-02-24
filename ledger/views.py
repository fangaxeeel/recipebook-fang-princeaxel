from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def recipe_list(request):
    template = loader.get_template('recipe_list.html')
    context = {
        "recipes": [
            {"name": "Recipe 1", "link": "/recipe/1/"},
            {"name": "Recipe 2", "link": "/recipe/2/"}
        ]
    }
    return HttpResponse(template.render(context, request))

def recipe_detail(request, num):
    recipes = {
        1: {
            "name": "Recipe 1",
            "ingredients": [
                {"name": "tomato", "quantity": "3pcs"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "pork", "quantity": "1kg"},
                {"name": "water", "quantity": "1L"},
                {"name": "sinigang mix", "quantity": "1 packet"}
            ],
            "link": "/recipe/1/"
        },
        2: {
            "name": "Recipe 2",
            "ingredients": [
                {"name": "garlic", "quantity": "1 head"},
                {"name": "onion", "quantity": "1pc"},
                {"name": "vinegar", "quantity": "1/2 cup"},
                {"name": "water", "quantity": "1 cup"},
                {"name": "salt", "quantity": "1 tablespoon"},
                {"name": "whole black peppers", "quantity": "1 tablespoon"},
                {"name": "pork", "quantity": "1 kilo"}
            ],
            "link": "/recipe/2/"
        }
    }

    recipe = recipes.get(num, {"name": "No Recipe Found", "ingredients": [], "link": "#"})

    template = loader.get_template('recipe_detail.html')
    return HttpResponse(template.render({"recipe": recipe}, request))
