import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm
from django.contrib import messages
from .models import Accounts
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator


@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Hash the password
            hashed_password = make_password(form.cleaned_data['password1'])

            new_account = Accounts.objects.create(
                login=form.cleaned_data['username'],
                password=hashed_password,  # Save the hashed password
                email=form.cleaned_data['email'],
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


@csrf_protect
def password_reset_request(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        email = request_data['email']
        try:
            account = Accounts.objects.get(email=email)
            if account:
                print(account.email)
                token = account.generate_reset_token()
                reset_link = f"https://lineage2hiro.com/reset/{token}"

                # Send email with reset link
                send_mail(
                    'Password reset',
                    f'Click the following link to reset your password: {reset_link}',
                    'from@example.com',
                    [email],
                    fail_silently=False,
                )

                print(token)
                print(reset_link)
                return JsonResponse({'success': True})
        except Accounts.DoesNotExist:
            return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': False})


@csrf_protect
def password_reset_confirm(request, token):
    try:
        # Decoding the token
        decoded_token = urlsafe_base64_decode(token).decode()

        # Extract UID and email from the decoded token
        uid, email = decoded_token.split('-')  # Assuming the token format is 'uid-email'

        # Get the user based on the UID
        user = Accounts.objects.get(pk=uid)  # Fetch the user using the UID

        if user.email == email:
            return redirect('password_reset_form')
        else:
            return JsonResponse('Invalid token. Email mismatch.')
    except (TypeError, ValueError, OverflowError, Accounts.DoesNotExist, IndexError):
        return JsonResponse('Password reset link is invalid or has expired.')
