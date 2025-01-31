from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def chat_home(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'chat/chat_home.html', {'users': users})

@login_required
def chat_room(request, room_name):
    return render(request, 'chat/chat_room.html', {'room_name': room_name})
