# Generated by Django 2.2.18 on 2021-02-07 11:50

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartapp', '0012_auto_20210207_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketerdetail',
            name='credits',
            field=models.CharField(default='not given', max_length=20, verbose_name=django.contrib.auth.models.User),
        ),
    ]
