from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    profile = models.ImageField(upload_to='profiles/', blank=True, null=True)
    DOB = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    fav_blogs = models.ManyToManyField('Blog', blank=True, null=True)

    def __str__(self):
        return self.username


class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name='blog_comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comments')
    content = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"
