# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-03-15 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segments', '0005_auto_20190314_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='recalculated_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
