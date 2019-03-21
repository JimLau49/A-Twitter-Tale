# Generated by Django 2.1.7 on 2019-03-20 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_private_message_private_message_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitter_tweet',
            name='content',
            field=models.TextField(default=None, max_length=140),
        ),
        migrations.AlterField(
            model_name='twitter_tweet',
            name='published',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
