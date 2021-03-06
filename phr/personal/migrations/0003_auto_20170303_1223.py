# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 12:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0002_auto_20170303_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoPersonal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_personal', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='personal',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='personal',
            name='establecimientos',
            field=models.ManyToManyField(blank=True, to='establecimiento.Establecimiento'),
        ),
        migrations.AddField(
            model_name='personal',
            name='tipo_personal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personal.TipoPersonal'),
        ),
    ]
