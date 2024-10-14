
from django.urls import path
from .views import login_view, registration_view
urlpatterns = [
    path('login/', login_view.handle_login, name='login'),
    path('register/', registration_view.handle_reg, name='register')
]
