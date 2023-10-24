from django.db.models import *


class Accounts(Model):
    login = CharField(primary_key=True, max_length=32, unique=True)
    password = CharField(max_length=255)
    last_access = IntegerField()
    access_level = IntegerField()
    last_ip = CharField(max_length=15, blank=True, null=True)
    last_server = IntegerField()
    bonus = IntegerField()
    bonus_expire = IntegerField()
    ban_expire = IntegerField()
    allow_ip = CharField(max_length=255)
    allow_hwid = CharField(max_length=255)
    points = IntegerField()
    phone_nubmer = BigIntegerField()

    class Meta:
        managed = False
        db_table = 'accounts'
        app_label = 'accounts'
