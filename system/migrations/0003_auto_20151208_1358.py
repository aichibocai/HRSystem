# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_info_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='manager',
            field=models.CharField(max_length=255),
        ),
    ]
