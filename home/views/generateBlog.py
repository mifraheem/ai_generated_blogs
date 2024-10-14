from django.shortcuts import render, redirect
from utils.ai import generate_blog
from django.contrib import messages
from authz.models import Blog
from django.contrib.auth.decorators import login_required


@login_required
def generate_blog_vew(request):
    if not request.user.is_superuser:
        messages.info(request, "Only Admin Can Generate the Blog")
        return redirect('home')
    if request.method == 'POST':
        title = request.POST.get('title')
        blog = generate_blog(title=title)
        context = {
            'generated_blog': blog,
            'generated_title': title
        }
        print(title)
        return render(request, "generate_blog.html", context)
    return render(request, "generate_blog.html")


@login_required
def save_blog(request):
    if request.method != 'POST':
        messages.warning(request, "Invalid Request")
        return redirect('home')

    title = request.POST.get('title')
    content = request.POST.get('content')
    image = request.FILES.get('image')

    blog = Blog.objects.create(title=title, content=content,  image=image)

    messages.success(request, "Blog Saved Successfully")
    return redirect('generate_blog')
