# Generated by Django 4.2.2 on 2023-06-22 17:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 22, 17, 11, 43, 713920, tzinfo=datetime.timezone.utc)),
        ),
    ]
