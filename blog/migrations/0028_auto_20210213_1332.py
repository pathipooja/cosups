# Generated by Django 2.2.18 on 2021-02-13 08:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0027_posttoearncredits'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostToEarnCredits',
            new_name='EarnCredits',
        ),
    ]