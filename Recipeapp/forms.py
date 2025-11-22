from django import forms
from .models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
class ChefForm(forms.ModelForm):
    class Meta:
        model = Chef
        fields = "__all__"
class ChefRecipeForm(forms.ModelForm):
    class Meta:
        model = ChefRecipe
        fields = "__all__"