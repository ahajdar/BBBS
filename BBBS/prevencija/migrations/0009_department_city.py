# Generated by Django 3.2.7 on 2021-09-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prevencija', '0008_alter_child_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='city',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]