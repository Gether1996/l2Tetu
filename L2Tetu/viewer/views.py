import json
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import uuid
from .forms import SignUpForm
from django.contrib.auth import logout
from .models import Character, Wallet
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
            user = form.save()
            new_wallet = Wallet.objects.create(user=user)
            new_wallet.save()
            return redirect('homepage')
        else:
            messages.error(request, 'Something went wrong.')
            return render(request, 'registration.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'registration.html', {'form': form})


@login_required
def account(request):
    logged_user = request.user
    wallet = Wallet.objects.get(user=logged_user)
    chars = Character.objects.filter(user=logged_user)
    json_data_chars = [
        {
            'id': str(char.id),
            'name': str(char.name),
            'coins': str(char.coins)
        }
        for char in chars
    ]
    json_data_wallet = {'coins': str(wallet.coins)}

    context = {
        'chars': chars,
        'json_data_chars': json_data_chars,
        'json_data_wallet': json_data_wallet
    }
    return render(request, 'account.html', context)


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

    request.session['coins'] = coins

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
    coins = request.session.get('coins')
    if coins and request.user.is_authenticated:
        user = request.user
        wallet = Wallet.objects.get(user=user)
        wallet.coins += int(coins)
        wallet.save()
        del request.session['coins']
    return render(request, 'payment_ok.html')


def fail(request):
    del request.session['coins']
    return render(request, 'payment_fail.html')


@csrf_exempt
@login_required
def transfer_coins(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        coins = request_data['transferAmount']

        wallet = Wallet.objects.get(user=request.user)
        char = Character.objects.get(id=request_data['charId'])
        print(f"{coins} transfering to {char.name}")

        wallet.coins -= int(coins)
        char.coins += int(coins)
        wallet.save()
        char.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})
