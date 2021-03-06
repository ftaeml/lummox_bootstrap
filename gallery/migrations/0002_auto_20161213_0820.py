# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-13 08:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Type'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='limn',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
