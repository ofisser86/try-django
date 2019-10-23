from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    title = "Hello Django"
    return render(request, 'index.html', {'title': title})


def contact_page(request):
    return render(request, 'index.html', {'title': "Contact page"})


def about_page(request):
    return render(request, 'index.html', {"title": "About page"})



