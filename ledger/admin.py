from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ("user", "name", "bio")

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient
    list_display = ('name',)

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    list_display = ('name', "author", "created_on", "updated_on")

class RecipeIngredientAdmin(admin.ModelAdmin):
    model = RecipeIngredient
    list_display = ('recipe', 'ingredient', 'quantity')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(RecipeIngredient, RecipeIngredientAdmin)