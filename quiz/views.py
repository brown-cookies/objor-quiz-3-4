from django.http import HttpRequest
from django.shortcuts import render


def index_page(request: HttpRequest):
    return render(request, "pages/index.html")
