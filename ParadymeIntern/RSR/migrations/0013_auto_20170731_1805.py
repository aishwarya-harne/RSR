# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-31 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RSR', '0012_person_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='Comments',
            field=models.CharField(default='Add Comment...', max_length=500),
        ),
    ]