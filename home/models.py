from distutils.command.upload import upload
import json
from django.db.models import Model
from django.db import models

# Create your models here.
class Ingredients(models.Model):
    id = models.AutoField(primary_key=True)
    ingredient = models.CharField(max_length=15)

    def __str__(self):
        return "{} {}".format(self.id, self.ingredient)


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    ingredients = models.CharField(max_length=100)
    recipe = models.TextField()

    def __str__(self):
        return "{} {}".format(self.id, self.ingredients)

