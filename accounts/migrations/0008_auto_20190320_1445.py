# Generated by Django 2.1.7 on 2019-03-20 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_profile_user_encrypt_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='user_profile_picture',
            field=models.ImageField(blank=True, default='default_user.png', upload_to='profile_image'),
        ),
    ]