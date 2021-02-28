# Generated by Django 2.2.5 on 2020-07-13 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=30)),
                ('phonenumber', models.IntegerField(default=18)),
                ('email', models.EmailField(max_length=30)),
                ('Type_of_community', models.CharField(max_length=30)),
                ('no_of_blocks', models.IntegerField(default=0)),
                ('no_of_flats_or_houses', models.IntegerField()),
                ('currentbill', models.CharField(max_length=30)),
                ('adhaarnumber', models.IntegerField()),
                ('partner', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('state', models.IntegerField()),
                ('district', models.IntegerField()),
                ('sub_colony', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]