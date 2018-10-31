# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-29 23:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resourcesApp', '0003_recurso_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso_comentario',
            name='revisor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='responsable', to='resourcesApp.Responsable'),
            preserve_default=False,
        ),
    ]
