# Generated by Django 3.2.7 on 2021-09-22 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prevencija', '0009_department_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinator',
            name='education',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='department',
            name='education',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='education',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]