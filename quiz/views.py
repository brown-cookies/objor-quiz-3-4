from .forms import RegisterUserForm
from django.http import HttpRequest
from django.shortcuts import redirect, render


def index_page(request: HttpRequest):
    return render(request, "pages/index.html")

def login_page(request: HttpRequest):
    return render(request, "pages/login.html")

def logout_page(request: HttpRequest):
    return render(request, "pages/logout.html")

def register_page(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RegisterUserForm()
    
    return render(request, 'pages/register.html', {'form': form})