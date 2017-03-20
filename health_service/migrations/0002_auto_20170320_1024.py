# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-20 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthfacility',
            name='catchment_areas',
            field=models.ManyToManyField(related_name='_healthfacility_catchment_areas_+', to='simple_locations.Area'),
        ),
    ]