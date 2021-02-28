# Generated by Django 2.2.18 on 2021-02-11 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20210211_2043'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesLoad',
            fields=[
                ('username', models.CharField(default='anu', max_length=256)),
                ('email', models.CharField(default='anu', max_length=256)),
                ('username_contesttitle', models.CharField(default='anu', max_length=256, primary_key=True, serialize=False)),
                ('contest_title', models.CharField(default='anu', max_length=256)),
                ('files', models.FileField(blank=True, upload_to='files')),
            ],
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('username', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256)),
                ('username_contesttitle', models.CharField(default='anu', max_length=256, primary_key=True, serialize=False)),
                ('contest_title', models.CharField(max_length=256)),
                ('participate', models.BooleanField(default=False)),
            ],
        ),
    ]