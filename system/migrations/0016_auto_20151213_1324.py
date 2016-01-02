# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0015_auto_20151212_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dno', models.CharField(max_length=100)),
                ('manager', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='info',
            name='manager',
        ),
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(to='system.department'),
        ),
    ]
