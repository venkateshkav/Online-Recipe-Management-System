from django.urls import path
from .views import *


urlpatterns = [
    path('category/',category_data, name="category"),
    path('category/edit/<int:ct_id>/',edit_category, name="edit_ct"),
    path('category/del/<int:ct_id>/',delete_category, name="del_ct"),
    path('recipe/',recipe_data, name="recipe"),
    path('recipe/edit/<int:re_id>/',edit_recipe, name="edit_re"),
    path('recipe/del/<int:re_id>/',delete_recipe, name="del_re"),
    path('chef/',chef_data, name="chef"),
    path('chef/edit/<int:ch_id>/',edit_chef, name="edit_ch"),
    path('chef/del/<int:ch_id>/',delete_chef , name="del_ch"),
    path('chefrecipe/',chefrecipe_data, name="chefrecpe"),
    path('dashboard/',filter_data,name="dashboard"),
]