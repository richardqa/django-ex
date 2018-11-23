# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-12 11:04
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('insteducativa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucioneducativa',
            name='tipo',
        ),
        migrations.AddField(
            model_name='institucioneducativa',
            name='nivel',
            field=models.CharField(choices=[('1', 'Inicial'), ('2', 'Primaria'), ('3', 'Secundaria')], default='3',
                                   max_length=1),
        ),
        migrations.AddField(
            model_name='institucioneducativa',
            name='ubicacion',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326,
                                                                 verbose_name='longitud/latitud'),
        ),
    ]