# Generated by Django 5.1.3 on 2024-12-12 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0019_remove_activity_exercise'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='calories_burned',
            field=models.FloatField(blank=True, null=True),
        ),
    ]