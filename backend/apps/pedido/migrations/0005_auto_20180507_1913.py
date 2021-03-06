# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-07 19:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_auto_20180507_1855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='id',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='pedido.Cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entrega',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.Pedido'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='codigo',
            field=models.AutoField(default=None, primary_key=True, serialize=False),
        ),
    ]
