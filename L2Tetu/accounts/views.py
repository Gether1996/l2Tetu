from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from .models import Accounts
from django.contrib.auth.hashers import make_password


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Hash the password
            hashed_password = make_password(form.cleaned_data['password1'])

            new_account = Accounts.objects.create(
                login=form.cleaned_data['username'],
                password=hashed_password,  # Save the hashed password
                last_ip=get_client_ip(request),
            )
            return redirect('homepage')
        else:
            messages.error(request, 'Something went wrong.')
            return render(request, 'registration.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip