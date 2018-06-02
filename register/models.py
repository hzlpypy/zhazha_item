from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=32,unique=True,null=True)
    password = models.CharField(max_length=32,null=True)

    class Meta:
        db_table = 'user'

###############################################

# class Change(models.Model):
#     class Meta:
#         abstract = True  # abstract	boolean类型	说明:是否建表	继承:不继承，子类自动充值为默认值(False)
#
#     def to_dict(self):
#         dic = {}
#         for key in vars(self).keys():
#             if not key.startswith('_'):
#                 things = getattr(self, key)
#                 if isinstance(things, datetime.datetime):
#                     dic[key] = datetime.datetime.strftime(things, '%Y%m%d %H%M%S')
#                 elif isinstance(things, datetime.date):
#                     dic[key] = datetime.datetime.strftime(things, '%Y%m%d ')
#                 elif isinstance(things, Decimal):
#                     dic[key] = float(things)
#                 else:
#                     dic[key] = things
#         return dic
#
#     @staticmethod
#     def qs_to_dict(qs=None):
#         li = []
#         if isinstance(qs, QuerySet):
#             li = [models.to_dict() for models in qs]
#         return li
#
#
# class DjangoMigrations(Change):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class Gamedirectory(Change):
#     game_name = models.CharField(max_length=64, blank=True, null=True)
#     gid = models.ForeignKey('SmallTitle', models.DO_NOTHING, db_column='gid', blank=True, null=True,
#                             related_name='game')
#     sid = models.ForeignKey('Headbranch', models.DO_NOTHING, db_column='sid', blank=True, null=True,
#                             related_name='pagegame')
#     info = models.CharField(max_length=255)
#
#     class Meta:
#         managed = False
#         db_table = 'gamedirectory'
#
#
# class My_img(Change):
#     img_name = models.CharField(max_length=64, blank=True)
#     mid = models.ForeignKey('Gamedirectory', models.DO_NOTHING, db_column='mid', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'my_img'
#
#
# class Headbranch(Change):
#     main_branch = models.CharField(max_length=64, blank=True, null=True)
#     mid = models.ForeignKey('Headgame', models.DO_NOTHING, db_column='mid', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'headbranch'
#
#
# class Headgame(Change):
#     oneinfor = models.CharField(max_length=64, blank=True, null=True)
#     cid = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'headgame'
#
#
# class LinkInfor(Change):
#     samll_title = models.CharField(max_length=32)
#     matter = models.CharField(max_length=32, blank=True, null=True)
#     cid = models.ForeignKey('YysSmallInfor', models.DO_NOTHING, db_column='cid', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'link_infor'
#
#
# class SmallTitle(Change):
#     content = models.CharField(max_length=64, blank=True, null=True)
#     tid = models.ForeignKey(Headbranch, models.DO_NOTHING, db_column='tid', blank=True, null=True)
#     pid = models.IntegerField(blank=True, null=True)
#     title_list = {}
#
#     class Meta:
#         managed = False
#         db_table = 'small_title'
#
#
# class Start(Change):
#     gg = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'start'
#
#
# class User(Change):
#     username = models.CharField(unique=True, max_length=32, blank=True, null=True)
#     password = models.CharField(max_length=32, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'user'
#
#
# class YysSmallInfor(Change):
#     small_infor = models.CharField(unique=True, max_length=200)
#     uid = models.ForeignKey('Yysinfor', models.DO_NOTHING, db_column='uid', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'yys_small_infor'
#
#
# class Yysinfor(Change):
#     title = models.CharField(max_length=32)
#
#     class Meta:
#         managed = False
#         db_table = 'yysinfor'