from django.contrib import admin

# Register your models here.

from .models import Exercise # models.py (aynı klasörde o nedenle . ile eriştik) dosyasındaki modelleri içe aktarır

admin.site.register(Exercise)