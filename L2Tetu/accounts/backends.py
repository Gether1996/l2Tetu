from django.contrib.auth.backends import ModelBackend
from .models import Accounts


class CustomAccountsBackend(ModelBackend):
    def authenticate(self, request, login=None, password=None, **kwargs):
        try:
            # Check if a user with the given login and password exists
            user = Accounts.objects.get(login=login, password=password)
        except Accounts.DoesNotExist:
            return None  # User not found or password is incorrect
        return user  # Authentication succeeded
