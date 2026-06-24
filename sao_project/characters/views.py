from django.shortcuts import render


def ListCharacters(request):
    return render(request, 'characters/characters_card.html')
