# Generated by Django 3.1.4 on 2022-02-19 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20220219_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, default='profile_pictures/default_profile_picture.jpg', null=True, upload_to='profile_pictures'),
        ),
    ]
