# Generated by Django 3.2.7 on 2021-09-22 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prevencija', '0005_alter_child_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='volunteerreport',
            options={'verbose_name_plural': 'Volonterski izvještaji'},
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('date_completed', models.DateTimeField(blank=True, null=True)),
                ('coordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prevencija.coordinator')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prevencija.department')),
                ('volunteer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prevencija.volunteer')),
            ],
            options={
                'verbose_name_plural': 'Organizacija volonetera',
            },
        ),
    ]