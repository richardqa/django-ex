# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ubigeo', '0003_auto_20170301_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='ubigeopais',
            name='id_pais',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
    ]
