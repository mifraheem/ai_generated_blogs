from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from authz.models import Blog, Comments


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, "index.html", context)


def blog_detail(request, blogid):
    singl_blog = Blog.objects.filter(id=blogid).first()
    blog_comments = Comments.objects.filter(blog=singl_blog)
    context = {'blog': singl_blog,
               'comments': blog_comments
               }
    return render(request, 'blog_details.html', context)
