# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20180328_2312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='account',
        ),
        migrations.DeleteModel(
            name='Account',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]
