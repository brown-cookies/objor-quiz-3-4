from .forms import LoginUserForm, RegisterUserForm
from account.forms import ProfileUpdateForm
from account.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import UpdateView


def index_page(request: HttpRequest):
    return render(request, "pages/index.html")

def login_page(request: HttpRequest):
    print(request.method)
    if request.method == "POST":
        form = LoginUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginUserForm()

    return render(request, 'pages/login.html', {'form': form})

def logout_page(request: HttpRequest):
    logout(request)
    return redirect('login')

def register_page(request: HttpRequest):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            Profile.objects.create(user=user)
            
            return redirect('index')
    else:
        form = RegisterUserForm()
    
    return render(request, 'pages/register.html', {'form': form})

@login_required()
def profile_page(request: HttpRequest):
    return render(request, 'pages/profile.html')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'pages/update-profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['last_donation_date'].widget.attrs['readonly'] = True
        return form