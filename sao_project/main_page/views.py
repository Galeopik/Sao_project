from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def CharacterInfo(request):
    return render(request, '')