# Generated by Django 5.1.3 on 2024-12-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0026_alter_activity_calories_per_minute'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='calories_per_minute',
            field=models.IntegerField(default=0, help_text='Kcal', null=True),
        ),
    ]