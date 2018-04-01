# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20180328_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('account_number', models.CharField(unique=True, max_length=11)),
                ('opening_date', models.DateTimeField(auto_now_add=True)),
                ('balance', models.DecimalField(max_digits=20, decimal_places=2)),
                ('mail_id', models.EmailField(null=True, blank=True, max_length=100)),
                ('mobile_number', models.CharField(null=True, blank=True, max_length=10)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transctions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('tranction_type', models.CharField(choices=[('C', 'credit'), ('D', 'debit')], max_length=1, default='C')),
                ('tranction_date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('customer', models.ForeignKey(to='myapp.Customer')),
            ],
        ),
    ]
