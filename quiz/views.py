from django.http import HttpRequest
from django.shortcuts import render


def index_page(request: HttpRequest):
    return render(request, "pages/index.html")

def login_page(request: HttpRequest):
    return render(request, "pages/login.html")

def logout_page(request: HttpRequest):
    return render(request, "pages/logout.html")

def register_page(request: HttpRequest):
    return render(request, "pages/register.html")
