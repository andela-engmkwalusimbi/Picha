# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 13:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160218_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='effectsmodel',
            old_name='photo_id',
            new_name='photo',
        ),
    ]