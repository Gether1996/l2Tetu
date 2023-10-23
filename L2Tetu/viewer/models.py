from django.contrib.auth.models import User
from django.db.models import *


# class Wallet(Model):
#     user = ForeignKey(User, on_delete=CASCADE)
#     coins = BigIntegerField(default=0)


class Characters(Model):
    account_name = CharField(max_length=45)
    obj_id = IntegerField(db_column='obj_Id', primary_key=True)  # Field name made lowercase.
    char_name = CharField(unique=True, max_length=35)
    face = PositiveIntegerField(blank=True, null=True)
    beautyface = PositiveSmallIntegerField(db_column='beautyFace', blank=True, null=True)  # Field name made lowercase.
    hairstyle = PositiveIntegerField(db_column='hairStyle', blank=True, null=True)  # Field name made lowercase.
    beautyhairstyle = PositiveSmallIntegerField(db_column='beautyHairStyle', blank=True, null=True)  # Field name made lowercase.
    haircolor = PositiveIntegerField(db_column='hairColor', blank=True, null=True)  # Field name made lowercase.
    beautyhaircolor = PositiveSmallIntegerField(db_column='beautyHairColor', blank=True, null=True)  # Field name made lowercase.
    sex = IntegerField(blank=True, null=True)
    x = IntegerField(blank=True, null=True)
    y = IntegerField(blank=True, null=True)
    z = IntegerField(blank=True, null=True)
    karma = IntegerField(blank=True, null=True)
    pvpkills = IntegerField(blank=True, null=True)
    pkkills = IntegerField(blank=True, null=True)
    clanid = IntegerField(blank=True, null=True)
    createtime = PositiveIntegerField()
    deletetime = PositiveIntegerField()
    title = CharField(max_length=16, blank=True, null=True)
    rec_have = PositiveIntegerField()
    rec_left = PositiveIntegerField()
    accesslevel = IntegerField(blank=True, null=True)
    online = IntegerField(blank=True, null=True)
    onlinetime = PositiveIntegerField()
    lastaccess = PositiveIntegerField(db_column='lastAccess')  # Field name made lowercase.
    leaveclan = PositiveIntegerField()
    deleteclan = PositiveIntegerField()
    nochannel = IntegerField()
    pledge_type = SmallIntegerField()
    pledge_rank = PositiveIntegerField()
    lvl_joined_academy = PositiveIntegerField()
    apprentice = PositiveIntegerField()
    key_bindings = CharField(max_length=8192, blank=True, null=True)
    pcbangpoints = IntegerField(db_column='pcBangPoints')  # Field name made lowercase.
    fame = IntegerField()
    bookmarks = PositiveIntegerField()
    bot_rating = IntegerField()
    used_world_chat_points = IntegerField()
    hide_head_accessories = PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'characters'


class Items(Model):
    object_id = IntegerField(primary_key=True)
    owner_id = IntegerField()
    item_id = IntegerField()
    count = BigIntegerField()
    enchant_level = IntegerField()
    loc = CharField(max_length=32)
    loc_data = IntegerField()
    life_time = IntegerField()
    custom_type1 = IntegerField()
    custom_type2 = IntegerField()
    custom_flags = IntegerField()

    class Meta:
        managed = False
        db_table = 'items'
