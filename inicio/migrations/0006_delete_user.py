# Generated by Django 4.1 on 2022-10-13 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0005_rename_username_user_usern'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
    ]