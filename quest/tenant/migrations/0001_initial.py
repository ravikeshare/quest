# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 10:42
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=100)),
                ('api_key', models.CharField(max_length=20, unique=True)),
                ('daily_access_limit', models.IntegerField(default=100)),
                ('remaining_access_count', models.IntegerField(default=100)),
                ('throttle', models.IntegerField(default=1)),
                ('throttle_duration', models.IntegerField(default=10, help_text='Throttle limit duration in seconds')),
            ],
            options={
                'abstract': False,
                'ordering': ('-modified', '-created'),
                'get_latest_by': 'modified',
            },
        ),
    ]