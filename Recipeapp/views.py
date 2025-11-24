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

def edit_category(request,ct_id):
    data = Category.objects.get(id=ct_id)
    form = CategoryForm(instance=data)
    if request.method == "POST":
        form = CategoryForm(instance=data,data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('category')
    return render(request,"edit_category.html",{"form":form})
def delete_category(request,ct_id):
    data = Category.objects.get(id=ct_id)
    data.delete()
    return redirect('category')

def recipe_data(request):
    form = RecipeForm()
    data = Recipe.objects.all()
    if request.method == "POST":
        form = RecipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"recipe.html",{"form":form,"data":data})

def edit_recipe(request,re_id):
    data = Recipe.objects.get(id=re_id)
    form = RecipeForm(instance=data)
    if request.method == "POST":
        form = RecipeForm(instance=data,data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('recipe')
    return render(request,"edit_recipe.html",{"form":form})

def delete_recipe(request,re_id):
    data = Recipe.objects.get(id=re_id)
    data.delete()
    return redirect('recipe')

def chef_data(request):
    form = ChefForm()
    data = Chef.objects.all()
    if request.method == "POST":
        form = ChefForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"chef.html",{"form":form,"data":data})

def edit_chef(request,ch_id):
    data = Chef.objects.get(id=ch_id)
    form = ChefForm(instance=data)
    if request.method == "POST":
        form = ChefForm(instance=data,data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('chef')
    return render(request,"edit_chef.html",{"form":form})

def delete_chef(request,ch_id):
    data = Chef.objects.get(id=ch_id)
    data.delete()
    return redirect('chef')

def chefrecipe_data(request):
    form = ChefRecipeForm()
    data = ChefRecipe.objects.all()
    if request.method == "POST":
        form = ChefRecipeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"chefrecipe.html",{"form":form,"data":data})

def filter_data(request):
    difficulty = Recipe.objects.filter(difficulty= "Easy")
    return render(request,"dashboard.html",{"difficulty":difficulty})

