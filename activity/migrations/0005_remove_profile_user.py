# Generated by Django 3.1.6 on 2021-02-10 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0004_auto_20210210_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]