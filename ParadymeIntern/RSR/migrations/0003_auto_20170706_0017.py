# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-06 00:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0002_auto_20170703_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person_company',
            name='EndDate',
            field=models.DateField(default=6, verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='person_company',
            name='StartDate',
            field=models.DateField(default=6, verbose_name='Start Date'),
        ),
    ]
