from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout
from .models import Character
from django.contrib.auth.decorators import login_required


def homepage(request):
    return render(request, 'homepage.html')


def logout_view(request):
    logout(request)
    return redirect('homepage')


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def account(request):
    logged_user = request.user
    chars = Character.objects.filter(user=logged_user)
    return render(request, 'account.html', {'chars': chars})


def forum(request):
    return render(request, 'forum.html')


@login_required
def donate(request):
    return render(request, 'donate.html')
