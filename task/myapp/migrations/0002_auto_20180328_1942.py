# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankaccount',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='transctions',
            name='bankaccount',
        ),
        migrations.DeleteModel(
            name='BankAccount',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Transctions',
        ),
    ]
