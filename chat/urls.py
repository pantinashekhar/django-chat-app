from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('chat/', views.chat, name='chat'),
    path('room/<str:room_name>/', views.room, name='room'),
]
