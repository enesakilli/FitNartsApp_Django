# Generated by Django 5.1.3 on 2024-12-12 09:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0015_remove_activity_exercise'),
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='exercise',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='exercise.exercise'),
        ),
    ]
