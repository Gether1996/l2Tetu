from django.contrib import admin
from .models import Wallet, Character


@admin.register(Wallet)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'coins', 'id')


@admin.register(Character)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'id', 'level', 'coins')

