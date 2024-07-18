from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required


def main(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login/')  # Redirige vers une page d'accueil ou une page spécifique
    else:
        form = SignUpForm()
    return render(request, 'signup_form.html', {'form': form})


@login_required
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def logout(request):
    logout(request)
    return redirect('login')




