# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-30 13:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20160927_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]