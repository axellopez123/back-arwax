from django.urls import path
from .views import BotsAPI

urlpatterns = [
    path('bots/', BotsAPI.as_view(), name='bots-api'),
]
