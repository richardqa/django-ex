# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-06 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ciudadano', '0057_auto_20171124_0929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudadano',
            name='numero_documento',
            field=models.CharField(blank=True, db_index=True, max_length=15, null=True, verbose_name='Número de documento'),
        ),
    ]
