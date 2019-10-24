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
