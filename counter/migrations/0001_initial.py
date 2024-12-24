# Generated by Django 5.1.3 on 2024-12-08 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('age_group', models.CharField(choices=[('<18', '<18'), ('18-30', '18-30'), ('30<', '30<')], max_length=5)),
                ('exercise_duration', models.IntegerField(help_text='Minute', validators=[django.core.validators.MinValueValidator(1)])),
                ('calories_per_minute', models.IntegerField(help_text='Kcal', validators=[django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Timer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('is_running', models.BooleanField(default=False)),
                ('elapsed_time', models.FloatField(default=0.0)),
            ],
        ),
    ]
