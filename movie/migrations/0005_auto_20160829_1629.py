# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-29 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20160829_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.FileField(upload_to=''),
        ),
    ]