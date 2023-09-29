from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout
from .models import Wallet, Character


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


def account(request):
    logged_user = request.user
    wallet = Wallet.objects.get(user=logged_user)
    chars = Character.objects.filter(user=logged_user)
    return render(request, 'account.html', {'wallet': wallet, 'chars': chars})


def forum(request):
    return render(request, 'forum.html')


def donate(request):
    logged_user = request.user
    wallet = Wallet.objects.get(user=logged_user)
    return render(request, 'donate.html', {'wallet': wallet})
