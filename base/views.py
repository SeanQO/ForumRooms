from django.shortcuts import render

rooms = [
    {'id': 1, 'name': "python"},
    {'id': 2, 'name': "java"},
    {'id': 3, 'name': "sql"},
    {'id': 4, 'name': "django"}
]


def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)


def room(request, pk):
    room_context = None

    for r in rooms:
        if r['id'] == int(pk):
            room_context = r

    context = {'room': room_context}
    return render(request, 'room.html', context)
