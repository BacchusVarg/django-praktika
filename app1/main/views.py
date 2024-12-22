from django.shortcuts import render

def index(request):
    context = {
        'title': 'EnglishLVL',
        'content': 'Главная страница',
    }
    return render(request, 'main/index.html', context)
