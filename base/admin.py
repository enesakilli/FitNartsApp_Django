from django.contrib import admin

# Register your models here.

from .models import UserProfile # models.py (aynı klasörde o nedenle . ile eriştik) dosyasındaki modelleri içe aktarır

admin.site.register(UserProfile) 
# Admin paneli, modelleri yönetmek için bir arayüz sağlar 
# Django'nun admin paneline modelleri kaydetmek için kullanılır.
# Admin panelinde veri ekleme, güncelleme ve silme işlemleri yapılır