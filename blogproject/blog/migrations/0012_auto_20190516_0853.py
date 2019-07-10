# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-05-16 00:53
from __future__ import unicode_literals

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190515_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='body',
            field=mdeditor.fields.MDTextField(verbose_name='博主信息'),
        ),
    ]