from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_home(request):
    return Response({'message': 'Welcome to the real-time chat API!'})


def chat_room(request):
    return render(request, 'chat.html')


