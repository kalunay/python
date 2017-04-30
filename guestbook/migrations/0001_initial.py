# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-25 21:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guestbook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20, verbose_name='Users')),
                ('posted', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Public')),
                ('content', models.TextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'запись гостевой книги',
                'ordering': ['-posted'],
                'verbose_name_plural': 'записи гостевой книги',
            },
        ),
    ]
