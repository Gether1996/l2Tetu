from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .forms import SignUpForm
from django.contrib.auth import logout
from .models import Character
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings


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


def donate(request):
    if request.method == "POST":
        coin_value = request.POST.get("coins")
        dollar_value = request.POST.get("dollar-cost")

        # Now you can use coin_value and dollar_value when constructing the PayPal dictionary
        # Replace "amount" and "item_name" with these values in the dictionary

        # Convert dollar_value to a numeric format (removing the '$' sign)
        dollar_value = float(dollar_value.replace('$', ''))

        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": dollar_value,  # Use dollar_value here
            "item_name": f"{coin_value} Coins",  # Set the item name to "Coins"
            "invoice": "unique-invoice-id",  # Unique invoice ID
            "currency_code": "USD",
            "notify_url": settings.PAYPAL_IPN_URL,
            "return_url": "http://localhost:8000/thank-you/",  # Redirect after successful payment
            "cancel_return": "http://localhost:8000/cancel/",
        }

        form = PayPalPaymentsForm(initial=paypal_dict)
        paypal_url = f"https://www.sandbox.paypal.com/cgi-bin/webscr?{'&'.join([f'{k}={v}' for k, v in paypal_dict.items()])}"
        print(paypal_url)
        return redirect(paypal_url)
    return render(request, 'donate.html')
