from django.urls import path
from .views import show_datetime

urlpatterns = [
    path('', show_datetime, name='show_datetime'),  # agora '/' mostra data e hora
]