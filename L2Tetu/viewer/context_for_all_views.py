# from .models import Wallet
# from django.contrib.auth.models import AnonymousUser
#
#
# def wallet_context(request):
#     if isinstance(request.user, AnonymousUser):
#         wallet = None
#     else:
#         try:
#             wallet = Wallet.objects.get(user=request.user)
#         except Wallet.DoesNotExist:
#             wallet = Wallet.objects.create(user=request.user)
#
#     return {'wallet': wallet}