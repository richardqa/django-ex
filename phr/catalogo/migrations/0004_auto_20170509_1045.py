# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-09 10:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0003_auto_20170509_1044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogoprocedimiento',
            old_name='denominacion_procedimientos',
            new_name='denominacion_procedimiento',
        ),
    ]
