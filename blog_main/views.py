
from django.shortcuts import render

from blogs.models import blog, Category
from biography.models import About

def home(request):
    featured_posts = blog.objects.filter(is_featured=True, status='published').order_by('updated_at')
    posts = blog.objects.filter(is_featured=False, status='published')
    
#fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }           
    return render(request, 'home.html', context)