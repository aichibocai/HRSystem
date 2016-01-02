# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0020_auto_20151214_0917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='check',
            options={'ordering': ['date']},
        ),
        migrations.AlterModelOptions(
            name='salary',
            options={'ordering': ['date'], 'permissions': ('change_salary', 'Change salary')},
        ),
        migrations.AlterField(
            model_name='info',
            name='department',
            field=models.ForeignKey(to='system.Department'),
        ),
    ]
