from django.urls import path
from .views import *


urlpatterns = [
    path('category/',category_data, name="category"),
    path('recipe/',recipe_data, name="recipe"),
]