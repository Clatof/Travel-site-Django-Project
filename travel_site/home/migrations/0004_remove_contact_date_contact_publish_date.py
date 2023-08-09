# Generated by Django 4.2.2 on 2023-08-09 04:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date',
        ),
        migrations.AddField(
            model_name='contact',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
