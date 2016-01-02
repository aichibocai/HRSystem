# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0023_auto_20151215_1123'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='check',
            options={'ordering': ['date'], 'permissions': (('department_manager', 'Department manager'),)},
        ),
        migrations.AlterModelOptions(
            name='salary',
            options={'ordering': ['date'], 'permissions': (('update_salary', 'Update salary'), ('department_manager', 'Department manager'))},
        ),
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(to='system.Department'),
        ),
    ]
