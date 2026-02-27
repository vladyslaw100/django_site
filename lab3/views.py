from django.shortcuts import render

def index(request):
    context = {
        'message': 'Це головна сторінка'
    }
    return render(request, 'lab3/index.html', context)

def page1(request):
    context = {
        'message': 'Це перша сторінка'
    }
    return render(request, 'lab3/page1.html', context)

def page2(request):
    context = {
        'message': 'Це друга сторінка'
    }
    return render(request, 'lab3/page2.html', context)