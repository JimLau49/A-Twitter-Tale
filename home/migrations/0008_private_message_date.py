# Generated by Django 2.1.7 on 2019-03-18 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20190318_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='private_message',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
