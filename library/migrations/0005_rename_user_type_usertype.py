# Generated by Django 4.0 on 2022-02-28 17:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_user_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_type',
            new_name='UserType',
        ),
    ]