# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-20 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0008_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='extension',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
