# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-05-19 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, null=True, unique=True)),
                ('password', models.CharField(max_length=32, null=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
