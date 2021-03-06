# Generated by Django 3.1.2 on 2020-11-03 14:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0003_auto_20201103_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='date_added',
            field=models.DateField(default=datetime.datetime(2020, 11, 3, 14, 18, 33, 241169, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(default=None, upload_to='uploads/%d-%m-%y'),
        ),
    ]
