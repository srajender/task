# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('account_number', models.CharField(max_length=11, unique=True)),
                ('opening_date', models.DateTimeField(auto_now_add=True)),
                ('balance', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('customer_name', models.CharField(max_length=100)),
                ('mail_id', models.EmailField(max_length=100, null=True, blank=True)),
                ('mobile_number', models.CharField(max_length=10, null=True, blank=True)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Transctions',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('bankaccount', models.ManyToManyField(to='myapp.BankAccount')),
            ],
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='customer',
            field=models.ForeignKey(to='myapp.Customer'),
        ),
    ]
