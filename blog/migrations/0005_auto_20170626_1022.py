# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170626_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]
