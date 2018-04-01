# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_auto_20180328_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('account_number', models.CharField(max_length=10, unique=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('date_of_open', models.DateField(auto_now_add=True)),
                ('mail_id', models.EmailField(max_length=100, null=True, blank=True)),
                ('mobile_number', models.CharField(max_length=10, null=True, blank=True)),
                ('address', models.TextField()),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
        ),
    ]
