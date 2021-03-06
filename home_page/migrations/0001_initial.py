# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-01 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Gamedirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(blank=True, max_length=64, null=True)),
                ('info', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'gamedirectory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Headbranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_branch', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'headbranch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Headgame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oneinfor', models.CharField(blank=True, max_length=64, null=True)),
                ('cid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'headgame',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='JumpHtm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_game', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'jump_htm',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LinkInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('samll_title', models.CharField(max_length=32)),
                ('matter', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'link_infor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='My_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_name', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'db_table': 'my_img',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SmallTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=64, null=True)),
                ('pid', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'small_title',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Start',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gg', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'start',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=32, null=True, unique=True)),
                ('password', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Yysinfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'yysinfor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YysSmallInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_infor', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'yys_small_infor',
                'managed': False,
            },
        ),
    ]
