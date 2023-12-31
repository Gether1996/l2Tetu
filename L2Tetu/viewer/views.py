import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import uuid
from django.contrib.auth import logout, authenticate, login
from .models import Characters, Items
from django.contrib.auth.decorators import login_required
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


def homepage(request):
    return render(request, 'homepage.html')


def logout_view(request):
    logout(request)
    return redirect('homepage')


def news(request):
    return render(request, 'news.html')


@csrf_protect
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('account')
        else:
            messages.error(request, 'Wrong login or password.')
            return render(request, 'registration/login.html')
    return JsonResponse({'success': False, 'message': 'Invalid request method'})


@login_required
def account(request):
    if hasattr(request.user, 'login'):
        chars = Characters.objects.filter(account_name=request.user.login)
        json_data_user_coins = {'user_coins': request.user.points}
    else:
        chars = None
        json_data_user_coins = {}
    item_id_to_count = 4037  # Specify the item_id you want to count - COLs

    json_data_chars = []

    if chars:
        for char in chars:
            try:
                item = Items.objects.get(owner_id=char.obj_id, item_id=item_id_to_count)
                item_count = item.count
            except Items.DoesNotExist:
                item_count = 0

            json_data_chars.append({
                'id': str(char.obj_id),
                'name': str(char.char_name),
                'COLs': item_count
            })

    context = {
        'json_data_chars': json_data_chars,
        'json_data_user_coins': json_data_user_coins
    }
    return render(request, 'account.html', context)


@login_required
def donate(request):
    return render(request, 'donate.html')


@login_required
def checkout(request):
    coins = request.GET.get('coins')
    dollars = request.GET.get('dollars')

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
    bought_coins = coins
    if coins and request.user.is_authenticated:
        user = request.user
        user.points += int(coins)
        user.save()
        del request.session['coins']
    return render(request, 'payment_ok.html', {'coins': bought_coins})


def fail(request):
    del request.session['coins']
    return render(request, 'payment_fail.html')


@login_required
def transfer_coins(request):
    if request.method == 'POST':
        request_data = json.loads(request.body)
        coins = request_data['transferAmount']
        item_id_to_count = 4037  # COLs

        user = request.user
        char = Characters.objects.get(obj_id=request_data['charId'])
        cols_item = Items.objects.get(owner_id=char.obj_id, item_id=item_id_to_count)
        print(f"{coins} transfering to {char.char_name}")

        user.points -= int(coins)
        cols_item.count += int(coins)
        user.save()
        cols_item.save()
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"})