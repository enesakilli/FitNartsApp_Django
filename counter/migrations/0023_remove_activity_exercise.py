# Generated by Django 5.1.3 on 2024-12-13 12:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0022_activity_exercise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='exercise',
        ),
    ]
