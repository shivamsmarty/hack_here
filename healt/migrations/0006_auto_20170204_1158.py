# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 11:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('healt', '0005_auto_20170204_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthofficer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='healthOfficer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='healthofficer',
            name='city',
            field=models.ManyToManyField(related_name='healthOfficer', to='healt.City'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userProfile', to=settings.AUTH_USER_MODEL),
        ),
    ]
