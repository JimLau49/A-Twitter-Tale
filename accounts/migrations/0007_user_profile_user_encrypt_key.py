# Generated by Django 2.1.7 on 2019-03-19 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190316_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='user_encrypt_key',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
