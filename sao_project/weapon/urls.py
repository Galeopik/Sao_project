from django.urls import path
from . import views

app_name = 'weapons'

urlpatterns = [
    path('', views.ListWeapons, name='list_weapons'),
]