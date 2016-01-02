# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0019_auto_20151213_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='birth',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(to='system.Department'),
        ),
    ]
