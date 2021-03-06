# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-10 16:35
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ubigeo', '0006_auto_20170310_1635'),
        ('ciudadano', '0026_ciudadanoparentesco'),
    ]

    operations = [
        migrations.AddField(
            model_name='ciudadano',
            name='departamento_domicilio_actual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='departamento_domicilio_actual', to='ubigeo.UbigeoDepartamento'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='distrito_domicilio_actual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='distrito_domicilio_actual', to='ubigeo.UbigeoDistrito'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='domicilio_direccion_actual',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Direccion Actual'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='domicilio_referencia_actual',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Domicilio Referencia Actual'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='localidad_domicilio_actual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='localidad_domicilio_actual', to='ubigeo.UbigeoLocalidad'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='pais_domicilio_actual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='pais_domicilio_actual', to='ubigeo.UbigeoPais'),
        ),
        migrations.AddField(
            model_name='ciudadano',
            name='provincia_domicilio_actual',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    related_name='provincia_domicilio_actual', to='ubigeo.UbigeoProvincia'),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='domicilio_direccion',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Domicilio Direccion'),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='domicilio_referencia',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Domicilio Referencia'),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='estado_civil',
            field=models.CharField(blank=True, choices=[('1', 'Soltero(a)'), ('2', 'Casado(a)'), ('3', 'Conviviente'),
                                                        ('4', 'Divorciado(a)'), ('5', 'Viudo(a)')], default='1',
                                   max_length=2, null=True, verbose_name='Estado civil'),
        ),
        migrations.AlterField(
            model_name='ciudadano',
            name='origen_datos',
            field=models.PositiveSmallIntegerField(blank=True,
                                                   choices=[(1, 'local'), (2, 'hisminsa'), (3, 'busqueda reniec')],
                                                   default=1, null=True),
        ),
    ]
