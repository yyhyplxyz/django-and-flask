# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-05 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20171205_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filedb',
            name='source',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='choice',
            field=models.CharField(choices=[('dislike', 'dislike'), ('like', 'like'), ('normal', 'normal')], max_length=10),
        ),
    ]
