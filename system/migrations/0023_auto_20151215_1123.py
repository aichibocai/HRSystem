# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0022_auto_20151215_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='salary',
            options={'ordering': ['date'], 'permissions': (('update_salary', 'Update salary'),)},
        ),
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(to='system.Department'),
        ),
    ]
