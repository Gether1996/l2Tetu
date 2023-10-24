from django.contrib import admin
from .models import Characters, Items


@admin.register(Characters)
class CharactersAdmin(admin.ModelAdmin):
    list_display = ('char_name', 'obj_id', 'account_name')


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'owner_id', 'item_id', 'count')
