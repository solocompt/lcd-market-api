# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-04-04 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20170404_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Product'),
        ),
    ]