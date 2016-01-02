# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(default=datetime.datetime(2015, 12, 8, 3, 22, 55, 606875, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
