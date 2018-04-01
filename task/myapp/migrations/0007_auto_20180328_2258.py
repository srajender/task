# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20180328_2257'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(unique=True)),
                ('date_of_open', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(blank=True, max_length=100, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=10, null=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_type', models.CharField(choices=[('C', 'credit'), ('D', 'debit')], max_length=1, default='C')),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(to='myapp.Customer'),
        ),
        migrations.AddField(
            model_name='account',
            name='transaction',
            field=models.ForeignKey(to='myapp.Transactions'),
        ),
    ]
