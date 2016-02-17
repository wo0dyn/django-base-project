# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-16 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('url', models.CharField(blank=True, max_length=400, null=True)),
                ('target', models.PositiveSmallIntegerField(choices=[(1, b'_self'), (2, b'_blank')], default=1)),
                ('sort_order', models.PositiveIntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menus.MenuItem')),
            ],
            options={
                'ordering': ['sort_order'],
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
            },
        ),
    ]
