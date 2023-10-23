# Generated by Django 4.2.1 on 2023-10-23 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characters',
            fields=[
                ('account_name', models.CharField(max_length=45)),
                ('obj_id', models.IntegerField(db_column='obj_Id', primary_key=True, serialize=False)),
                ('char_name', models.CharField(max_length=35, unique=True)),
                ('face', models.PositiveIntegerField(blank=True, null=True)),
                ('beautyface', models.PositiveSmallIntegerField(blank=True, db_column='beautyFace', null=True)),
                ('hairstyle', models.PositiveIntegerField(blank=True, db_column='hairStyle', null=True)),
                ('beautyhairstyle', models.PositiveSmallIntegerField(blank=True, db_column='beautyHairStyle', null=True)),
                ('haircolor', models.PositiveIntegerField(blank=True, db_column='hairColor', null=True)),
                ('beautyhaircolor', models.PositiveSmallIntegerField(blank=True, db_column='beautyHairColor', null=True)),
                ('sex', models.IntegerField(blank=True, null=True)),
                ('x', models.IntegerField(blank=True, null=True)),
                ('y', models.IntegerField(blank=True, null=True)),
                ('z', models.IntegerField(blank=True, null=True)),
                ('karma', models.IntegerField(blank=True, null=True)),
                ('pvpkills', models.IntegerField(blank=True, null=True)),
                ('pkkills', models.IntegerField(blank=True, null=True)),
                ('clanid', models.IntegerField(blank=True, null=True)),
                ('createtime', models.PositiveIntegerField()),
                ('deletetime', models.PositiveIntegerField()),
                ('title', models.CharField(blank=True, max_length=16, null=True)),
                ('rec_have', models.PositiveIntegerField()),
                ('rec_left', models.PositiveIntegerField()),
                ('accesslevel', models.IntegerField(blank=True, null=True)),
                ('online', models.IntegerField(blank=True, null=True)),
                ('onlinetime', models.PositiveIntegerField()),
                ('lastaccess', models.PositiveIntegerField(db_column='lastAccess')),
                ('leaveclan', models.PositiveIntegerField()),
                ('deleteclan', models.PositiveIntegerField()),
                ('nochannel', models.IntegerField()),
                ('pledge_type', models.SmallIntegerField()),
                ('pledge_rank', models.PositiveIntegerField()),
                ('lvl_joined_academy', models.PositiveIntegerField()),
                ('apprentice', models.PositiveIntegerField()),
                ('key_bindings', models.CharField(blank=True, max_length=8192, null=True)),
                ('pcbangpoints', models.IntegerField(db_column='pcBangPoints')),
                ('fame', models.IntegerField()),
                ('bookmarks', models.PositiveIntegerField()),
                ('bot_rating', models.IntegerField()),
                ('used_world_chat_points', models.IntegerField()),
                ('hide_head_accessories', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'characters',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('object_id', models.IntegerField(primary_key=True, serialize=False)),
                ('owner_id', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('count', models.BigIntegerField()),
                ('enchant_level', models.IntegerField()),
                ('loc', models.CharField(max_length=32)),
                ('loc_data', models.IntegerField()),
                ('life_time', models.IntegerField()),
                ('custom_type1', models.IntegerField()),
                ('custom_type2', models.IntegerField()),
                ('custom_flags', models.IntegerField()),
            ],
            options={
                'db_table': 'items',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='user',
        ),
        migrations.DeleteModel(
            name='Character',
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
