# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-28 12:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20170227_1931'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='electronics', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.CharField(default='product_1.jpg', max_length=200),
            preserve_default=False,
        ),
    ]
