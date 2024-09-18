from .forms import LoginUserForm, RegisterUserForm
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import redirect, render


def index_page(request: HttpRequest):
    return render(request, "pages/index.html")

def login_page(request: HttpRequest):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        
        print('post req')
        if form.is_valid():
            print('valid')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        print('get req')
        
        form = LoginUserForm()

    return render(request, 'pages/login.html', {'form': form})

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