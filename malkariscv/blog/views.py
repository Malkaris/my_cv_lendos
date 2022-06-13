from django.shortcuts import render
from .models import Blog
# Create your views here.


def blog(request):
    blog_list = Blog.objects.order_by('-id')
    dict_blog = {'blog_list': blog_list}
    return render(request, './blog.html', dict_blog)