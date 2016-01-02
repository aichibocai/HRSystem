# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20151209_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='sex',
            field=models.CharField(default=b'ml', max_length=10, choices=[(b'ml', b'male'), (b'fml', b'female')]),
        ),
    ]
