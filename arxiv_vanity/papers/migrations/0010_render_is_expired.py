# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("papers", "0009_auto_20171020_1015")]

    operations = [
        migrations.AddField(
            model_name="render",
            name="is_expired",
            field=models.BooleanField(default=False),
        )
    ]
