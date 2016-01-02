# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20151209_1313'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(max_length=4)),
                ('month', models.IntegerField(max_length=2)),
                ('Salary', models.FloatField()),
                ('info', models.ForeignKey(to='system.Info')),
            ],
        ),
    ]
