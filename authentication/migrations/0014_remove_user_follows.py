# Generated by Django 4.0.1 on 2022-02-26 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follows',
        ),
    ]