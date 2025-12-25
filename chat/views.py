from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, Message
from .forms import MessageForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
        else:
            # Handle invalid login
            return render(request, 'chat/login.html', {'error': 'Invalid credentials'})
    return render(request, 'chat/login.html')


@login_required
def chat(request):
    rooms = ChatRoom.objects.all()
    return render(request, 'chat/chat.html', {'rooms': rooms})

@login_required
def room(request, room_name):
    room = ChatRoom.objects.get(name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.save(commit=False)
            message.room = room
            message.user = request.user
            message.save()
            return redirect('room', room_name=room_name)
    else:
        form = MessageForm()
    return render(request, 'chat/room.html', {'room': room, 'messages': messages, 'form': form})
