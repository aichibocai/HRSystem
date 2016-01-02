# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0017_auto_20151213_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(to='system.Department'),
        ),
    ]
