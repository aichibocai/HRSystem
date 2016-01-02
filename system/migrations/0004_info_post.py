# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20151208_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='post',
            field=models.CharField(default=datetime.datetime(2015, 12, 9, 7, 28, 40, 863142, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
