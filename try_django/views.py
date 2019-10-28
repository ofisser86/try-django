from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template


def home_page(request):
    title = "Hello Django"
    context = {'title': title, 'my_list': [1, 2, 3, 4, 5]}
    return render(request, 'index.html', context)


def contact_page(request):
    print(request.POST)
    return render(request, 'contact.html', {'title': "Contact page"})


def about_page(request):
    return render(request, 'about.html', {"title": "About page"})


def render_txt(request):
    context = {'title': "Txt title render"}
    template_name = 'text.txt'
    template_obj = get_template(template_name)
    template_item = template_obj.render(context)
    return HttpResponse(template_item)
