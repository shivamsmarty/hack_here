# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healt', '0006_auto_20170204_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='affected_city',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
