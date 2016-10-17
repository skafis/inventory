# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 10:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('unit_measure', models.CharField(max_length=100)),
                ('no_of_units', models.IntegerField()),
                ('period_of_measure', models.CharField(max_length=100)),
                ('purchased_inventory', models.IntegerField()),
                ('usage', models.IntegerField()),
                ('closing_inventory', models.IntegerField()),
            ],
        ),
    ]
