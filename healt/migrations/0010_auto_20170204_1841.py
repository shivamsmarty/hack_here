# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healt', '0009_auto_20170204_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='posted_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]