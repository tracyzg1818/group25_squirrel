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

def edit_squirrel(request, squirrel_id):

    squirrel = show.objects.get(Unique_squirrel_id = squirrel_id)

    if request.method == 'POST':
        form = SquirrelForm(request.POST,instance=squirrel)
        if form.is_valid():
            form.save()
            messages.success(request, "You successfully updated the Squirrel")

            return redirect(f'/sightings/')
    else:
        form = SquirrelForm(instance=squirrel)

    context = {'form':form,}
    return render(request, 'sightings/edit.html',context)

def add_squirrel(request):
    if request.method == 'POST':
        form = SquirrelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SquirrelForm()
    context = {'form':form,}
    return render(request, 'sightings/add.html',context)

def stats(request):
    all_squirrels_num = show.objects.all().count()
    per_adult_squirrels = (show.objects.filter(Age='Adult').count()/show.objects.all().count())*100
    per_running_squirrels = (show.objects.filter(Running=True).count()/show.objects.all().count())*100
    per_gray_squirrels= (show.objects.filter(Primary_fur_color='Gray').count()/show.objects.all().count())*100
    per_eating_squirrels =(show.objects.filter(Eating=True).count()/show.objects.all().count())*100

    context = {'all_squirrels_num': all_squirrels_num,
               'per_adult_squirrels':per_adult_squirrels,
               'per_gray_squirrels':per_gray_squirrels,
               'per_running_squirrels': per_running_squirrels,
               'per_eating_squirrels':per_eating_squirrels}

    return render(request, 'sightings/stats.html',context)
