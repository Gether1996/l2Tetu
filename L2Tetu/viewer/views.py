from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import logout


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
    return render(request, 'account.html')


def forum(request):
    return render(request, 'forum.html')


def donate(request):
    return render(request, 'donate.html')
