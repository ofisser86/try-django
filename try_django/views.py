from django.http import HttpResponse


def home_page(request):
    return HttpResponse("Hello Django")


def contact_page(request):
    return HttpResponse("Contact")


def about_page(request):
    return HttpResponse("<h1>About page</h1>")



