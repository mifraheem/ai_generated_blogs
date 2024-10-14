
from django.urls import path
from .views import home_view
from .views import generateBlog
urlpatterns = [
    path('', home_view.home, name='home'),
    path('generate-blog/', generateBlog.generate_blog_vew, name='generate_blog'),
    path('save-blog/', generateBlog.save_blog, name='save_blog')

]
