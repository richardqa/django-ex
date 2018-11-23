# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-24 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20170421_1813'),
        ('ciudadano', '0030_auto_20170417_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='AntecedenteCiudadano',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('tipo_antecedente', models.CharField(choices=[('1', 'Personal'), ('2', 'Gineco-Obstetra'), ('3', 'Patológico'), ('4', 'Psicológico')], max_length=1)),
                ('ciex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.CatalogoCIE')),
                ('ciudadano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciudadano.Ciudadano')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AntecedenteFamiliar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('es_removido', models.BooleanField(default=False, editable=False)),
                ('parentesco', models.PositiveSmallIntegerField(choices=[(1, 'Padre'), (2, 'Madre'), (3, 'Hijo'), (4, 'Hija')])),
                ('fecha_inicio', models.DateField(blank=True)),
                ('fecha_fin', models.DateField(blank=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('ciex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.CatalogoCIE')),
                ('ciudadano', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ciudadano.Ciudadano')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='ciudadanoparentesco',
            name='parentesco',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Padre'), (2, 'Madre'), (3, 'Hijo'), (4, 'Hija')]),
        ),
    ]