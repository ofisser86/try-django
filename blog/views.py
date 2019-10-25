from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import BlogPost
# Create your views here.


def blog_post_detail_page(request, slug):
    # obj = BlogPost.objects.get(slug=slug)
    # obj = get_object_or_404(BlogPost, slug=slug)
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() != 1:
        raise Http404
    obj = queryset.first()
    template_name = 'blog_post_detail_page.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    qs = BlogPost.objects.all() # Or could use .filter() is some specific data  need
    template_name = 'blog_post_list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_create_view(request):
    # Todo: Create form
    template_name = 'blog_post_create.html'
    context = {'form': None}
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_update.html'
    context = {'object': None, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog_post_delete.html'
    context = {'object': None}
    return render(request, template_name, context)
