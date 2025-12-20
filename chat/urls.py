from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.api_home, name='api_home'),
    path('chat/', views.chat_room, name='chat_room'),

]
