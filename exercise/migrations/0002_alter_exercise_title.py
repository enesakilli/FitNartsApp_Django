# Generated by Django 5.1.3 on 2024-12-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]
