# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_record', '0003_auto_20171202_0552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tbrecord',
            options={'managed': False, 'ordering': ['seq']},
        ),
    ]