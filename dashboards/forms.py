from django import forms
from blogs.models import Category, blog

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'



class BlogPostForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ('title','status','category','short_description', 'blog_body','featured_image', 'is_featured')
