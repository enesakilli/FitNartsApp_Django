# Generated by Django 5.1.3 on 2024-12-12 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0018_activity_exercise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='exercise',
        ),
    ]