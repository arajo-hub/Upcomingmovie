# Generated by Django 3.0.3 on 2020-05-09 11:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20200509_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_movie',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 5, 9, 20, 8, 18, 216335)),
        ),
    ]