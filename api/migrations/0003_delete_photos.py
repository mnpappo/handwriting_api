# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-15 23:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170615_2303'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photos',
        ),
    ]
