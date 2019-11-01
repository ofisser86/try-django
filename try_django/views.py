from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.db import models
from blog.models import BlogPost

from .forms import ContactForm


def home_page(request):
    title = "Welcome to try Django"
    template_name = 'home.html'
    qs = BlogPost.objects.all()[:5]
    context = {'title': title, 'blog_list': qs}
    # if request.user.is_authenticated:
    #     context = {'title': title, 'my_list': [1, 2, 3, 4, 5]}
    return render(request, template_name, context)


def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        'title': "Contact page",
        'form': form,
    }
    return render(request, 'contact.html', context)


def about_page(request):
    return render(request, 'about.html', {"title": "About page"})


def render_txt(request):
    context = {'title': "Txt title render"}
    template_name = 'text.txt'
    template_obj = get_template(template_name)
    template_item = template_obj.render(context)
    return HttpResponse(template_item)
