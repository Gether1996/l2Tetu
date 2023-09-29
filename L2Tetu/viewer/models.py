from django.contrib.auth.models import User
from django.db.models import *


class Wallet(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    coins = BigIntegerField(default=0)


class Character(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    name = CharField(max_length=50, blank=False)
    coins = BigIntegerField(default=0)
    level = IntegerField(default=1)
