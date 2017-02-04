# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='affected_age_group',
            field=models.CharField(choices=[('ch', 'Child'), ('teen', 'Teenagers'), ('adult', 'Adult'), ('old', 'Old')], max_length=20),
        ),
    ]