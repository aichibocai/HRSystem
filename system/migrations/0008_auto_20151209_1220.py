# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20151209_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='sex',
            field=models.CharField(default=b'ml', max_length=10, choices=[(b'ml', b'm'), (b'fml', b'f')]),
        ),
    ]
