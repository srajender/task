# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_customer_transctions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('tranction_type', models.CharField(choices=[('C', 'credit'), ('D', 'debit')], default='C', max_length=1)),
                ('tranction_date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('customer', models.ManyToManyField(to='myapp.Customer')),
            ],
        ),
        migrations.RemoveField(
            model_name='transctions',
            name='customer',
        ),
        migrations.DeleteModel(
            name='Transctions',
        ),
    ]
