from django.urls import path
from . import views

app_name = "main_page"

urlpatterns = [
    path("", views.index, name="index"),
    path("character/<int:pk>/", views.CharacterInfo, name="character_info"),
]
