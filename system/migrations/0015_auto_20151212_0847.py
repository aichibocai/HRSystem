# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0014_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary',
            name='month',
        ),
        migrations.RemoveField(
            model_name='salary',
            name='year',
        ),
        migrations.AddField(
            model_name='salary',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 12, 12, 8, 47, 13, 634356, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
