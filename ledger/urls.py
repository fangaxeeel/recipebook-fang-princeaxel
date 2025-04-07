from django.urls import path
from .views import recipe_list, recipe_detail, add_image, add_recipe
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipes/list/', recipe_list, name='recipe_list'),
    path('recipe/<int:num>/', recipe_detail, name='recipe_detail'),  
    path('recipe/<int:num>/add_image/', add_image, name='add_image'),
    path('recipe/add/', add_recipe, name='add_recipe'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
