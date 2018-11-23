# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 12:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ciudadano', '0022_ciudadano_origen_datos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudadano',
            name='origen_datos',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'local'), (2, 'hisminsa')], default=1,
                                                   null=True),
        ),
    ]
