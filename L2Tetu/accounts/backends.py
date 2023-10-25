from django.contrib.auth.backends import ModelBackend
from .models import Accounts
from django.contrib.auth.hashers import check_password


class CustomAccountsBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = Accounts.objects.filter(login=username).first()
        if user and check_password(password, user.password):
            return user  # Return the user instance
        return None

    def get_user(self, user_id):
        try:
            return Accounts.objects.get(pk=user_id)
        except Accounts.DoesNotExist:
            return None
