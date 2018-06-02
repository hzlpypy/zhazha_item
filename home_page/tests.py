from django.test import TestCase

# Create your tests here.



#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
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
# class Start(Change):
#     gg = models.CharField(max_length=255, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'start'
#
#
# class User(models.Model):
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
