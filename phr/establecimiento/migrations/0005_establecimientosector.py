# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-15 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('establecimiento', '0004_auto_20170308_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstablecimientoSector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('codigo', models.CharField(max_length=2)),
                ('descripcion', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
