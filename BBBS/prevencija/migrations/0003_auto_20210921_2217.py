# Generated by Django 3.2.7 on 2021-09-21 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prevencija', '0002_auto_20210921_2214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='volunteer',
        ),
        migrations.RemoveField(
            model_name='coordinator',
            name='department',
        ),
    ]
