from django import urls
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('game1', views.guess_game, name='guess_game'),
    path('pictures', views.testing, name='testing')
]