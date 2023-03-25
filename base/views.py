from django.shortcuts import render
from .models import *


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request, pk):
    r = Room.objects.get(id=pk)
    r = Room.objects.get(id=pk)
    context = {
        'room': r
    }
    return render(request, 'room.html', context)
