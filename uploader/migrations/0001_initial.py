# Generated by Django 3.1.2 on 2020-10-30 14:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=200)),
                ('path', models.CharField(default=None, max_length=100)),
                ('_type', models.CharField(default=None, max_length=100)),
                ('date_added', models.DateField(default=datetime.datetime(2020, 10, 30, 14, 25, 58, 366696, tzinfo=utc))),
            ],
        ),
    ]