# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadano', '0049_auto_20170821_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudadano',
            name='es_persona_viva',
            field=models.BooleanField(default=True),
        ),
    ]
