from ast import If
import json
from django.http import HttpResponse
from django.shortcuts import render,redirect

from home.models import Recipe

# Create your views here.
def home(request):
    return render(request, 'index.html')

def match(request):
    if request.method == 'POST':
        veggies = request.POST.getlist('veggies')
        ingredients = Recipe.objects.all()
        ingredients = {
            'veggies': veggies,
            'ingredients': ingredients
        }
        return render(request, 'recipe.html', ingredients)
    return HttpResponse("not selected")
