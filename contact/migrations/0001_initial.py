# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-27 02:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.CharField(max_length=30)),
                ('Twitter', models.CharField(max_length=25)),
                ('Github', models.CharField(max_length=15)),
                ('NoHp', models.IntegerField()),
            ],
        ),
    ]
