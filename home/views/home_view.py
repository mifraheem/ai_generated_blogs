from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages


def home(request):
    return render(request, "index.html")
