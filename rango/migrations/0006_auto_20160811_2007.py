# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-11 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_auto_20160811_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='first_visit',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='last_visit',
            field=models.DateField(auto_now=True),
        ),
    ]
