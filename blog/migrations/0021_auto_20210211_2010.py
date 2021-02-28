# Generated by Django 2.2.18 on 2021-02-11 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20200811_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='empty'),
        ),
        migrations.AddField(
            model_name='post',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
