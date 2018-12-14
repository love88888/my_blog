# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-12-12 03:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myxiangmu', '0005_auto_20181212_1126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, verbose_name='昵称')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myxiangmu.Blog', verbose_name='文章')),
            ],
        ),
    ]
