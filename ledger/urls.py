from django.urls import path
from .views import recipe_list, recipe_detail

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:num>/', recipe_detail, name='recipe_detail'),  
]
