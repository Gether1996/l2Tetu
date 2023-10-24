from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages
from .models import Accounts


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_account = Accounts.objects.create(
                login=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            return redirect('homepage')
        else:
            messages.error(request, 'Something went wrong.')
            return render(request, 'registration.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})
