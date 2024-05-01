from django.shortcuts import render, HttpResponse



# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def lolasdasdasd(request):
    return render(request, 'main/lol.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def articles(request):
    return render(request, 'main/articles.html')
