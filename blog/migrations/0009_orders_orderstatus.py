# Generated by Django 2.2.5 on 2020-07-13 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200713_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='orderstatus',
            field=models.CharField(default='In Process', max_length=32),
        ),
    ]
