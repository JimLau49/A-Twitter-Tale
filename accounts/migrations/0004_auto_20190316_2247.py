# Generated by Django 2.1.7 on 2019-03-17 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_profile_user_mails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='about_user',
            field=models.TextField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_city',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_country',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_email',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_first_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_last_name',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_phone',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='user_website',
            field=models.CharField(default=None, max_length=500),
        ),
    ]
