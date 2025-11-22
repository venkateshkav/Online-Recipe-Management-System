from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField()
    description = models.TextField()
    created_on = models.DateTimeField()

    def __str__(self):
        return self.name
class Recipe(models.Model):
    title = models.CharField()
    ingredients = models.TextField()
    steps = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    difficulty = models.CharField(choices=[("Easy","Easy"),("Medium","Medium"),("Hard","Hard")])
    created_on = models.DateField()
    image = models.ImageField(upload_to="img")
    recipe_file = models.FileField(upload_to="file")

class Chef(models.Model):
    chef_name = models.CharField()
    email = models.EmailField(unique=True)
    phone = models.PositiveIntegerField()
    experience = models.PositiveIntegerField()
    profile_photo = models.ImageField(upload_to="profile_photo")

    def __str__(self):
        return self.chef_name
    
class ChefRecipe(models.Model):
    chef = models.ForeignKey(Chef,on_delete=models.CASCADE,null=True,blank=True)
    recipe = models.ForeignKey(Recipe,on_delete=models.CASCADE,null=True,blank=True)
    created_date = models.DateField()

    