# Generated by Django 2.1.7 on 2019-03-17 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190316_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitter_tweet',
            name='media_attachment',
            field=models.ImageField(blank=True, default='default.png', upload_to='site_media'),
        ),
    ]
