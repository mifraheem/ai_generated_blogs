
from django.urls import path
from .views import home_view, comment_views
from .views import generateBlog
urlpatterns = [
    path('', home_view.home, name='home'),
    path('generate-blog/', generateBlog.generate_blog_vew, name='generate_blog'),
    path('save-blog/', generateBlog.save_blog, name='save_blog'),
    path('blog-detail/<int:blogid>', home_view.blog_detail, name='blog_detail'),


    # comments urls
    path('comment/<int:blogid>', comment_views.add_comment, name='add_comment'),

]
