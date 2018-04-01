# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20180328_2258'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='transaction',
        ),
        migrations.AddField(
            model_name='transactions',
            name='account',
            field=models.ManyToManyField(to='myapp.Account'),
        ),
    ]
