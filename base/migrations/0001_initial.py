# Generated by Django 5.1.3 on 2024-12-08 09:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6)),
                ('age', models.CharField(blank=True, max_length=3)),
                ('height', models.CharField(blank=True, max_length=3)),
                ('weight', models.CharField(blank=True, max_length=3)),
                ('profile_picture', models.ImageField(blank=True, default='images/default.png', null=True, upload_to='images/')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
