from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import BlogPost

# from .forms import BlogPostForm
from .forms import BlogPostModelForm
# Create your views here.


def blog_post_detail_page(request, slug):
    # obj = BlogPost.objects.get(slug=slug)
    # obj = get_object_or_404(BlogPost, slug=slug)
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() != 1:
        raise Http404
    obj = queryset.first()
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


def blog_post_list_view(request):
    qs = BlogPost.objects.all() # Or could use .filter() is some specific data  need
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {'object': obj}
    return render(request, template_name, context)


# @staff_member_required
@login_required  # use login_required(login='login.html') for redirect non-auth user to login page
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    # If use BlogPostForm  ---> obj = BlogPost.objects.create(**form.cleaned_data)
        form.save()
        # For data manipulate need to do:
        # obj = form.save(commit=False)
        # for example ---> obj.title = form.cleaned_data.get('title') + '0'  ==== add '0' to eac title

    # Reinitialize form
        form = BlogPostModelForm()
    context = {
        'title': "New post",
        'form': form,
    }
    template_name = 'blog/forms.html'
    return render(request, template_name, context)


def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/update.html'
    context = {'object': obj, 'form': None}
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    context = {'object': None}
    return render(request, template_name, context)
