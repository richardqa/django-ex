# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ciudadano', '0023_auto_20170301_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudadano',
            name='domicilio_direccion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio Direccion'),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='domicilio_referencia',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Domicilio Referencia'),
        ),
    ]
