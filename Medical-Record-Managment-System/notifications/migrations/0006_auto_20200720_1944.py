# Generated by Django 3.0.8 on 2020-07-20 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_auto_20200720_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='select_time',
            field=models.TimeField(default=datetime.datetime(2020, 7, 20, 19, 44, 21, 909579)),
        ),
    ]
