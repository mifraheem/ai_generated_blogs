from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login


def handle_login(request):
    if request.method != 'POST':
        messages.info(request, "Bad Request")
        return redirect('home')

    data = request.POST
    username = data.get('username')
    password = data.get('password')
    print(username, password)
    user = authenticate(request,  username=username, password=password)
    print(user)
    if user is not None:
        login(request, user)
        messages.success(request, f"Welcome, {user.username}")

    else:
        messages.info(request, "Invalid username or password")

    return redirect('home')
