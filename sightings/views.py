from django.shortcuts import render
from django.http import HttpResponse
from adopt.models import show
import random

def all_squirrels(request):
    squirrels = list(show.objects.all())
    context = {'squirrels': squirrels}
    return render(request, 'adopt/list_all.html', context)

