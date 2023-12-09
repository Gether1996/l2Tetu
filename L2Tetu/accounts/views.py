import json

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .forms import SignUpForm
from django.contrib import messages
from .models import Accounts
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_decode
import binascii


@csrf_protect
def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Check if the email is already registered
            try:
                already_regged_email = Accounts.objects.get(email=form.cleaned_data['email'])
                return render(request, 'registration.html', {'form': form, 'error_message': 'Email already registered'})
            except Accounts.DoesNotExist:
                # Email is not registered, continue with the registration process
                hashed_password = make_password(form.cleaned_data['password1'])
                new_account = Accounts.objects.create(
                    login=form.cleaned_data['username'],
                    password=hashed_password,
                    email=form.cleaned_data['email'],
                    last_ip=get_client_ip(request),
                )
                return redirect('homepage')
        else:
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


def password_reset_request(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        email = request_data['email']
        try:
            account = Accounts.objects.get(email=email)
            if account:
                print(account.email)
                token = account.generate_reset_token()
                reset_link = f"https://lineage2hiro.com/reset/{token}/"

                subject = 'L2Hiro password reset'
                message = f'Hello {account.login},\n\nClick the following link to reset your password: {reset_link}'
                from_email = 'gether1996@gmail.com'
                send_mail(subject, message, from_email, [email])


                print(token)
                print(reset_link)
                return JsonResponse({'success': True})
        except Accounts.DoesNotExist:
            return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': False})


def password_reset_confirm(request, token):
    uid = urlsafe_base64_decode(token).decode()
    user = Accounts.objects.get(id=uid)
    context = {
        'user': user
    }
    return render(request, 'password_reset_form.html', context)


def password_reset_confirm_post(request):
    if request.method == 'POST':
        try:
            request_data = json.loads(request.body)
            user_id = request_data['id']
            user = Accounts.objects.get(id=user_id)

            hashed_password = make_password(request_data['new_password'])
            user.password = hashed_password
            user.save()

            # Return a JsonResponse with the same structure as the try block
            return JsonResponse({'success': True})
        except (TypeError, ValueError, OverflowError, Accounts.DoesNotExist, IndexError, binascii.Error):
            # Return a JsonResponse with the same structure as the try block
            return JsonResponse({'error': 'Password reset link is invalid or has expired.'})
    else:
        return JsonResponse({'error': 'Invalid request method. Use POST for password reset confirmation.'})


def password_reset_success(request, user_id):
    user = Accounts.objects.get(id=user_id)
    return render(request, 'password_reset_success.html', {'user': user})
