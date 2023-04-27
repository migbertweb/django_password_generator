from django.shortcuts import render
# from django.http import HttpResponse


def home(request):
    return render(request, 'generator/home.html')


def about(request):
    return render(request, 'generator/about.html')


def password(request):
    return render(request, 'generator/password.html')
