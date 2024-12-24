# Generated by Django 5.1.3 on 2024-12-12 07:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0007_alter_activity_calories_per_minute_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='calories_per_minute',
            field=models.IntegerField(default=0, help_text='Kcal', null=True),
        ),
        migrations.AlterField(
            model_name='activity',
            name='exercise_duration',
            field=models.IntegerField(help_text='Minute', validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
