# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 15:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorylist', '0002_inventory_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='unit_measure',
            field=models.CharField(max_length=10),
        ),
    ]