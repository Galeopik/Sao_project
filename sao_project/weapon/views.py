from django.shortcuts import render


def ListWeapons(request):
    return render(request, 'weapons/weapon_card.html')
