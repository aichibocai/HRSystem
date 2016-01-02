# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20151209_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='manager',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
