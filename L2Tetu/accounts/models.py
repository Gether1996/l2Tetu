from django.db.models import *
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


class Accounts(Model):
    id = BigAutoField(primary_key=True)
    login = CharField(max_length=32, unique=True)
    password = CharField(max_length=255)
    email = CharField(max_length=50, null=True)
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


    def generate_reset_token(self):
        # Customize this method according to your Accounts model
        uid = urlsafe_base64_encode(force_bytes(self.pk))
        token = f'{uid}-{self.email}'  # You can customize this token generation based on your model's data
        return token
