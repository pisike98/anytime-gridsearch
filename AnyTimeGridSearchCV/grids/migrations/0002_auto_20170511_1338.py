# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-11 13:38
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvresult',
            name='cross_validation_scores',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(default=0.0), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='cvresult',
            name='gridsearch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='grids.GridSearch'),
        ),
    ]
