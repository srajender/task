# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('transaction_type', models.CharField(default='C', max_length=1, choices=[('C', 'credit'), ('D', 'debit')])),
                ('transaction_date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(max_digits=20, default=0.0, decimal_places=2)),
                ('customer', models.ForeignKey(to='myapp.Customer')),
            ],
        ),
    ]
