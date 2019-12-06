from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import SquirrelForm
from sightings.models import show
from django.contrib import messages
import random #for random

def all_squirrels(request):
    squirrels = list(show.objects.all())
    context = {'squirrels': squirrels}
    return render(request, 'sightings/list_all.html', context)

def map(request):
    map_100 = random.sample(range(show.objects.all().count()),100)
    map_squirrel = [show.objects.all()[i] for i in map_100]
    context = {'sightings':map_squirrel}
    return render(request, 'sightings/map.html',context)
