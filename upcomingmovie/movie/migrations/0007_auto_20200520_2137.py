# Generated by Django 3.0.6 on 2020-05-20 12:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20200520_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_movie',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 20, 21, 37, 37, 205991)),
        ),
    ]
