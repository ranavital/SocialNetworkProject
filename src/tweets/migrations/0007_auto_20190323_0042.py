# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-03-22 22:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20190322_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tweet',
            old_name='update',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='creation',
            new_name='updated',
        ),
    ]