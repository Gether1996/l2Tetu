from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import uuid
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


@login_required
def donate(request):
    return render(request, 'donate.html')


@login_required
def checkout(request):
    coins = request.GET.get('coins')
    dollars = request.GET.get('dollars')
    print(coins)
    print(dollars)

    host = request.get_host()

    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": dollars,  # Use dollar_value here
        "item_name": f"{coins} Coins",  # Set the item name to "Coins"
        "invoice": uuid.uuid4(),  # Unique invoice ID
        "currency_code": "USD",
        "notify_url": f"http://{host}{reverse('paypal-ipn')}",
        "return_url": f"http://{host}{reverse('success')}",
        "cancel_return": f"http://{host}{reverse('fail')}",
    }

    payment_paypal = PayPalPaymentsForm(initial=paypal_dict)
    context = {
        'coins': coins,
        'dollars': dollars,
        'paypal': payment_paypal
    }
    return render(request, 'checkout.html', context)


def success(request):
    return render(request, 'payment_ok.html')


def fail(request):
    return render(request, 'payment_fail.html')
