# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-11 14:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20160310_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='HiringManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=256)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Employee')),
            ],
        ),
    ]
