# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20180328_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('account_number', models.IntegerField(unique=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=20)),
                ('date_of_open', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(null=True, max_length=100, blank=True)),
                ('mobile_number', models.CharField(null=True, max_length=10, blank=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(default='C', max_length=1, choices=[('C', 'credit'), ('D', 'debit')])),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('account', models.ForeignKey(to='myapp.Account')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(to='myapp.Customer'),
        ),
    ]
