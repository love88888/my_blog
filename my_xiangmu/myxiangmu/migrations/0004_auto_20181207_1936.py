# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-07 11:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myxiangmu', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='blog',
        ),
    ]
