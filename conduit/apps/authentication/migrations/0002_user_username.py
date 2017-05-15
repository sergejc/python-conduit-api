# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-05-15 19:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(db_index=True, default=datetime.datetime(2017, 5, 15, 19, 13, 11, 33127, tzinfo=utc), max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
