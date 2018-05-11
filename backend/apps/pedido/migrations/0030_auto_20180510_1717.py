# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-10 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0029_auto_20180510_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='entrega',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='id',
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(default=0.09090909090909091, on_delete=django.db.models.deletion.CASCADE, to='pedido.Entrega'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='codigo',
            field=models.AutoField(default=None, primary_key=True, serialize=False, verbose_name='Codigo'),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]