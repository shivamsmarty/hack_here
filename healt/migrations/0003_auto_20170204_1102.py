# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 11:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('healt', '0002_auto_20170204_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthOfficer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
        migrations.AddField(
            model_name='query',
            name='posted_by',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='healt.UserProfile'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='query',
            name='verified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='healt.HealthOfficer'),
        ),
    ]
