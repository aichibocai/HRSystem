# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_auto_20151209_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='sex',
            field=models.CharField(default=b'male', max_length=10),
        ),
    ]
