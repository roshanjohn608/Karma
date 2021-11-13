# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-07 15:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('karma', '0008_auto_20180407_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentongoal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 48, 52, 816030)),
        ),
        migrations.AlterField(
            model_name='commentonprogress',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 48, 52, 817416)),
        ),
        migrations.AlterField(
            model_name='commentonproject',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 48, 52, 816766)),
        ),
        migrations.AlterField(
            model_name='goal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 48, 52, 811868)),
        ),
        migrations.AlterField(
            model_name='progress',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 48, 52, 815459)),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 48, 52, 814801)),
        ),
        migrations.AlterField(
            model_name='user',
            name='join_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 4, 7, 15, 48, 52, 810680)),
        ),
    ]
