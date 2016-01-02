# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0025_auto_20151215_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='check',
            options={'ordering': ['-date'], 'permissions': (('department_manager', 'Department manager'), ('HR_permission', 'HR permission'))},
        ),
        migrations.AlterModelOptions(
            name='salary',
            options={'ordering': ['-date'], 'permissions': (('update_salary', 'Update salary'), ('department_manager', 'Department manager'), ('HR_permission', 'HR permission'))},
        ),
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(to='system.Department'),
        ),
    ]
