# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='I like cats'),
            preserve_default=False,
        ),
    ]
