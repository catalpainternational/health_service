# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_locations', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthFacility',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=64, blank=True)),
                ('area', models.ForeignKey(related_name='facility+', blank=True, to='simple_locations.Area', null=True)),
                ('catchment_areas', models.ManyToManyField(related_name='_healthfacility_catchment_areas_+', null=True, to='simple_locations.Area', blank=True)),
                ('location', models.ForeignKey(blank=True, to='simple_locations.Point', null=True)),
            ],
            options={
                'verbose_name': 'Health Facility',
                'verbose_name_plural': 'Health Facilities',
            },
        ),
        migrations.CreateModel(
            name='HealthFacilityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'verbose_name': 'Health Facility Type',
                'verbose_name_plural': 'Health Facility Types',
            },
        ),
        migrations.CreateModel(
            name='OwnershipType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.CharField(unique=True, max_length=30)),
            ],
            options={
                'verbose_name': 'Ownership Type',
                'verbose_name_plural': 'Ownership Types',
            },
        ),
        migrations.AddField(
            model_name='healthfacility',
            name='ownership_type',
            field=models.ForeignKey(blank=True, to='health_service.OwnershipType', null=True),
        ),
        migrations.AddField(
            model_name='healthfacility',
            name='parent',
            field=models.ForeignKey(related_name='facility', blank=True, to='health_service.HealthFacility', null=True),
        ),
        migrations.AddField(
            model_name='healthfacility',
            name='type',
            field=models.ForeignKey(blank=True, to='health_service.HealthFacilityType', null=True),
        ),
    ]
