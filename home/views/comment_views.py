from django.shortcuts import render, redirect
from django.contrib import messages
from authz.models import *
from django.contrib.auth.decorators import login_required


@login_required
def add_comment(request, blogid):
    target_blog = Blog.objects.get(id=blogid)
    author = request.user
    content = request.POST.get('comment')
    comment = Comments.objects.create(
        blog=target_blog, author=author, content=content)
    messages.success(request, "Your comment has been saved.")
    return redirect('blog_detail',  blogid=blogid)
