# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-25 12:49
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ciudadano', '0033_ciudadano_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antecedenteciudadano',
            name='ciex',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='catalogo.CatalogoCIE'),
        ),
        migrations.AlterField(
            model_name='antecedenteciudadano',
            name='ciudadano',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ciudadano.Ciudadano'),
        ),
        migrations.AlterField(
            model_name='antecedenteciudadano',
            name='fecha_fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='antecedenteciudadano',
            name='fecha_inicio',
            field=models.DateField(blank=True, null=True),
        ),
    ]