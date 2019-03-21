# Generated by Django 2.1.7 on 2019-03-17 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20190316_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='about_user',
            field=models.TextField(blank=True, default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_city',
            field=models.CharField(blank=True, default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_country',
            field=models.CharField(blank=True, default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_email',
            field=models.CharField(blank=True, default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_first_name',
            field=models.CharField(blank=True, default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_last_name',
            field=models.CharField(blank=True, default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_phone',
            field=models.CharField(blank=True, default=' ', max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_website',
            field=models.CharField(blank=True, default=' ', max_length=500),
        ),
    ]
