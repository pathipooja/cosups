# Generated by Django 2.2.5 on 2020-07-25 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_orders_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='marketer_phonenumber',
            field=models.CharField(default='not given', max_length=10),
        ),
    ]
