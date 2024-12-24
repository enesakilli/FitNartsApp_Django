from django.db import models
from django.contrib.auth.models import User # Kullanıcı modeli: username password falan sağlıyor
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # OneToOneField, her UserProfile nesnesinin yalnızca bir kullanıcıya ait olmasını sağlar doğru mu
    name = models.CharField(max_length=30, blank=True)
    surname = models.CharField(max_length=30, blank=True)
    GENDER_CHOICES = [
        ('Female', 'Female'),
        ('Male', 'Male'),
    ]
    gender = models.CharField(max_length=6, blank=True, choices=GENDER_CHOICES) 
    age = models.CharField(max_length=3, blank=True)
    height = models.CharField(max_length=3, blank=True)
    weight = models.CharField(max_length=3, blank=True)
    profile_picture = models.ImageField( # Resim dosyaları için kullanılır, kullanıcının yüklediği resimlerin kaydedilmesini sağlar
        upload_to='images/', # ImageField edit profile kısmına fotoğraf için CLEAR butonu ekliyor
        null=True, # Veritabanında bu alanın boş olmasına izin verir
        blank=True, # Form doğrulamalarında alanın boş bırakılmasına izin verir
        default='images/default.png')
    # created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now = True) # Güncellenme tarihi, bir kaydın son güncellenme zamanını takip etmek için kullanılır
    created = models.DateTimeField(auto_now_add = True) # Oluşturulma tarihi, bir kaydın oluşturulma zamanını takip etmek için kullanılır

    def __str__(self):
        return self.user.username 