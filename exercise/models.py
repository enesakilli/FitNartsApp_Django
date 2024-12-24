from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    # Her bir task için User bulunması gerekiyor (many to one)
    # Olur da kullanıcı silinirse ona ait exercises silinmesi için CASCADE kullanıyorum
    title = models.CharField(max_length = 30, unique=True) 
    # Exercise için title gerekli 
    description = models.CharField(max_length = 500, unique=True)
    # Exercise için description gerekli 
    cals_per_minute = models.FloatField(null=True, blank=True) 
    # Dakika başına harcanan kalori
    created_at = models.DateTimeField(auto_now_add = True)
    # Exercise'ın oluşturulma tarihini ve saatini saklıyor
    image = models.ImageField(upload_to='images/', null=True, blank=True, default='images/no_image.png')
    # Fotoğraf ekleme
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.title
