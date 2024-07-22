from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib import messages
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


'''def loginType(request):
    form = SignUpForm(request.POST)
    user = form.save()
    login(request, user)
             # Détermine si l'utilisateur est un étudiant ou un enseignant
    if user.user_type == 2 :
        return redirect('accounts/profile/student_home')  # Assurez-vous que 'student_home' est défini dans urls.py
    elif user.user_type == 1 :
        return redirect('accounts/profile/teacher_home')  # Assurez-vous que 'teacher_home' est défini dans urls.py
    else:
        return redirect('login/')'''


def loginType(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.user_type == 2 :
                return redirect('accounts/profile/student_home')  # Assurez-vous que 'student_home' est défini dans urls.py
            elif user.user_type == 1 :
                return redirect('accounts/profile/teacher_home')  # Assurez-vous que 'teacher_home' est défini dans urls.py
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'login.html')


@login_required
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())


def logout(request):
    logout(request)
    return redirect('login')


@login_required
def student_home(request):
    return render(request, 'student_dashboard.html')


@login_required
def teacher_home(request):
    return render(request, 'teacher_dashboard.html')





