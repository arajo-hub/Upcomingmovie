# Generated by Django 3.0.3 on 2020-05-09 10:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, unique=True)),
                ('date', models.DateField(default=datetime.datetime(2020, 5, 9, 19, 31, 52, 76316))),
            ],
        ),
    ]
