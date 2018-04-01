# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20180328_2048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('account_number', models.IntegerField(unique=True)),
                ('balance', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='account_number',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='opening_date',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='customer',
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(to='myapp.Customer'),
        ),
        migrations.AddField(
            model_name='transactions',
            name='account',
            field=models.ManyToManyField(to='myapp.Account'),
        ),
    ]
