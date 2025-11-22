from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *


# Create your views here.
def category_data(request):
    form = CategoryForm()
    data = Category.objects.all()
    if request.method == "POST":
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"category.html",{"form":form,"data":data})

def recipe_data(request):
    form = RecipeForm()
    data = Recipe.objects.all()
    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"recipe.html",{"form":form,"data":data})

