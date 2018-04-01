# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20180328_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('account_number', models.IntegerField(unique=True)),
                ('balance', models.DecimalField(max_digits=20, decimal_places=2)),
                ('date_of_open', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(max_length=100, blank=True, null=True)),
                ('mobile_number', models.CharField(max_length=10, blank=True, null=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('transaction_type', models.CharField(max_length=1, default='C', choices=[('C', 'credit'), ('D', 'debit')])),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
                ('account', models.ManyToManyField(to='myapp.Account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(to='myapp.Customer'),
        ),
    ]
