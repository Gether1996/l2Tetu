from django.db.models import *


class Accounts(Model):
    id = BigAutoField(primary_key=True)
    login = CharField(max_length=32, unique=True)
    password = CharField(max_length=255)
    last_login = DateTimeField(null=True, blank=True)
    access_level = IntegerField(default=0)
    last_ip = CharField(max_length=15, blank=True, null=True)
    last_server = IntegerField(default=0)
    bonus = IntegerField(default=0)
    bonus_expire = IntegerField(default=0)
    ban_expire = IntegerField(default=0)
    allow_ip = CharField(max_length=255, default="")
    allow_hwid = CharField(max_length=255, default="")
    points = IntegerField(default=0)
    phone_number = BigIntegerField(default=0)
    is_staff = BooleanField(default=False)
    is_active = BooleanField(default=True)

    class Meta:
        managed = False
        db_table = 'accounts'
        app_label = 'accounts'

    @property
    def is_superuser(self):
        # Implement custom superuser check logic here
        return False  # Change to True if needed

    @property
    def is_authenticated(self):
        return self.id is not None
