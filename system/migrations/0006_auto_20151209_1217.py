# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0005_auto_20151209_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='manager',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='post',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='info',
            name='sex',
            field=models.CharField(default=b'ml', max_length=2, choices=[(b'ml', b'male'), (b'fml', b'female')]),
        ),
    ]
