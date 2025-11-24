from django.shortcuts import render,redirect,HttpResponse
from .models import *
from .forms import *
from django.db.models import Count, Avg, Max, Sum


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
        form = CategoryForm(request.POST,request.FILES,instance=data)
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
        form = RecipeForm(request.POST,request.FILES,instance=data)
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
        form = ChefForm(request.POST,request.FILES,instance=data)
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
    easy_recipes = Recipe.objects.filter(difficulty="Easy")
    desserts_recipes = Recipe.objects.filter(category__name="Desserts")
    prep_lt_cook = Recipe.objects.filter(prep_time__lt=models.F('cook_time'))
    experienced_chefs = Chef.objects.filter(experience__gt=5)

    # Aggregations
    recipes_count_category = Recipe.objects.values('category__name').annotate(count=Count('id'))
    recipes_count_chef = ChefRecipe.objects.values('chef__chef_name').annotate(count=Count('recipe'))
    avg_cook_time = Recipe.objects.aggregate(Avg('cook_time'))
    max_prep_time = Recipe.objects.aggregate(Max('prep_time'))
    total_chef_exp = Chef.objects.aggregate(Sum('experience'))

    context = {
        "easy_recipes": easy_recipes,
        "desserts_recipes": desserts_recipes,
        "prep_lt_cook": prep_lt_cook,
        "experienced_chefs": experienced_chefs,
        "recipes_count_category": recipes_count_category,
        "recipes_count_chef": recipes_count_chef,
        "avg_cook_time": avg_cook_time,
        "max_prep_time": max_prep_time,
        "total_chef_exp": total_chef_exp,
    }
    return render(request, "dashboard.html", context)



