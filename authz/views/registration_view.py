from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate
from authz.models import User


def handle_reg(request):
    if request.method != 'POST':
        messages.info(request, "Please Submit a form to Register")
        return redirect('home')

    data = request.POST
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    password2 = data.get('password2')
    print(username, email, password, password2)

    if password != password2:
        messages.warning(request, "Passwords don't match")
        return redirect('home')
    if User.objects.filter(username=username).exists():
        messages.warning(request, "Username already exists")
        return redirect('home')
    if User.objects.filter(email=email).exists():
        messages.warning(request, "Email already exists")
        return redirect('home')
    new_user = User.objects.create_user(
        username=username, email=email, password=password)
    new_user.save()
    messages.success(request, "Registration successful")
    return redirect('home')
