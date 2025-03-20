from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')  

def guess_game(request):
    return render(request, 'main/guess_game.html')  



