# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

import datetime

from decimal import Decimal
from django.db import models

##############################################
from django.db.models import QuerySet


class Change(models.Model):
    class Meta:
        abstract = True  # abstract	boolean类型	说明:是否建表	继承:不继承，子类自动充值为默认值(False)

    def to_dict(self):
        dic = {}
        for key in vars(self).keys():
            if not key.startswith('_'):
                things = getattr(self, key)
                if isinstance(things, datetime.datetime):
                    dic[key] = datetime.datetime.strftime(things, '%Y%m%d %H%M%S')
                elif isinstance(things, datetime.date):
                    dic[key] = datetime.datetime.strftime(things, '%Y%m%d ')
                elif isinstance(things, Decimal):
                    dic[key] = float(things)
                else:
                    dic[key] = things
        return dic

    @staticmethod
    def qs_to_dict(qs=None):
        li = []
        if isinstance(qs, QuerySet):
            li = [models.to_dict() for models in qs]
        return li


class DjangoMigrations(Change):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Gamedirectory(Change):
    game_name = models.CharField(max_length=64, blank=True, null=True)
    gid = models.ForeignKey('SmallTitle', models.DO_NOTHING, db_column='gid', blank=True, null=True,
                            related_name='game')
    sid = models.ForeignKey('Headbranch', models.DO_NOTHING, db_column='sid', blank=True, null=True,
                            related_name='pagegame')
    info = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'gamedirectory'


class My_img(Change):
    img_name = models.CharField(max_length=64, blank=True)
    mid = models.ForeignKey('Gamedirectory', models.DO_NOTHING, db_column='mid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'my_img'


class Headbranch(Change):
    main_branch = models.CharField(max_length=64, blank=True, null=True, verbose_name='游戏信息')
    mid = models.ForeignKey('Headgame', models.DO_NOTHING, db_column='mid', blank=True, null=True)

    def __str__(self):
        return self.main_branch

    class Meta:
        managed = False
        db_table = 'headbranch'


class Headgame(Change):
    oneinfor = models.CharField(max_length=64, blank=True, null=True, verbose_name='游戏主目录')
    cid = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.oneinfor

    class Meta:
        managed = False
        db_table = 'headgame'


class LinkInfor(Change):
    samll_title = models.CharField(max_length=32)
    matter = models.CharField(max_length=32, blank=True, null=True)
    cid = models.ForeignKey('YysSmallInfor', models.DO_NOTHING, db_column='cid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_infor'


class SmallTitle(Change):
    content = models.CharField(max_length=64, blank=True, null=True)
    tid = models.ForeignKey(Headbranch, models.DO_NOTHING, db_column='tid', blank=True, null=True)
    pid = models.IntegerField(blank=True, null=True)
    title_list = {}

    class Meta:
        managed = False
        db_table = 'small_title'


class Start(Change):
    gg = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'start'


class User(Change):
    username = models.CharField(unique=True, max_length=32, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class YysSmallInfor(Change):
    small_infor = models.CharField(unique=True, max_length=200)
    uid = models.ForeignKey('Yysinfor', models.DO_NOTHING, db_column='uid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yys_small_infor'


class Yysinfor(Change):
    title = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'yysinfor'


class JumpHtm(Change):
    jid = models.ForeignKey(Gamedirectory, models.DO_NOTHING, db_column='jid', blank=True, null=True)
    img_game = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jump_htm'
