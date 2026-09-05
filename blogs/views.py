from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .models import blog, Category
from django.db.models import Q

# Create your views here.

def post_by_category(request, category_id):
    posts = blog.objects.filter(status='published', category=category_id)
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)


def blogs(request, slug):
    single_blog = get_object_or_404(blog, slug=slug, status='published')
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')

    blogs = blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='published')
    context = {
        'blogs': blogs,
        'keyword': keyword
    }
    return render(request, 'search.html', context)