# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0012_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='Salary',
            new_name='salary',
        ),
        migrations.AlterField(
            model_name='info',
            name='birth',
            field=models.DateField(verbose_name=b'date published'),
        ),
        migrations.AlterField(
            model_name='salary',
            name='month',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='salary',
            name='year',
            field=models.IntegerField(),
        ),
    ]
