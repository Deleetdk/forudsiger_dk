# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-23 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160123_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='truth_conditions',
            field=models.TextField(),
        ),
    ]
