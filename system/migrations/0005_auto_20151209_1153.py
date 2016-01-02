# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_info_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='birth',
            field=models.DateField(default=datetime.datetime(2015, 12, 9, 11, 53, 42, 377254, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='sex',
            field=models.CharField(default=b'male', max_length=255),
        ),
    ]
