# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establecimiento', '0003_auto_20170307_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='microred',
            name='codigo',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='red',
            name='codigo',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='red',
            name='estado',
            field=models.CharField(blank=True, choices=[('1', 'Activo'), ('2', 'Inactivo'), ('3', 'Pendiente')], max_length=20, null=True),
        ),
    ]
