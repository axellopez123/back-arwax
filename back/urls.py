from django.urls import path
from .views import BotAPI

urlpatterns = [
    path('bot/', BotAPI.as_view(), name='bot-api'),
]
