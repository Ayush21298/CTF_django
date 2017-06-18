# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-18 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='solved',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]