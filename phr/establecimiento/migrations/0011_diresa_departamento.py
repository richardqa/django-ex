# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-15 10:43
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ubigeo', '0011_auto_20170508_1826'),
        ('establecimiento', '0010_auto_20170424_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='diresa',
            name='departamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='ubigeo.UbigeoDepartamento'),
        ),
    ]
