from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car' : 'BMW',
            'age' : 21,
            'hobby' : 'Wrestling'
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')