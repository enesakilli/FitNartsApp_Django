from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from exercise.models import Exercise

# Create your models here.

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activities')  # Kullanıcı ile ilişkilendiriyorum
    ACTIVITY_CHOICES = [ # Cinsiyet seçeneği için kullanılan sabit bir seçim kümesi
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    
    AGE_CHOICES = [ # Yaş grubu seçeneği için kullanılan sabit bir seçim kümesi
        ('<18', '<18'),
        ('18-30', '18-30'),
        ('30<', '30<'),
    ]
    
    gender = models.CharField(max_length=6, choices=ACTIVITY_CHOICES)
    age_group = models.CharField(max_length=5, choices=AGE_CHOICES)
    exercise_duration = models.IntegerField(help_text="Minute", validators=[MinValueValidator(1)])
    # Egzersizin süresini dakika cinsinden saklamak için IntegerField kullanır ve minimum değer 1 
    calories_per_minute = models.IntegerField(help_text="Kcal", null=True, default=0) # NULL yerine 0 atar, validators=[MinValueValidator(1)] ı kaldırdım çünkü default=0 olacak
    # calories_per_minute = models.IntegerField(help_text="Kcal", validators=[MinValueValidator(1)]) # exercise kcal/min girilmezse hesaplarken None olunca hata veriyor 
    # Her bir dakikada yakılan kalori miktarını saklamak için IntegerField kullanır ve minimum değer 1
    calories_burned = models.FloatField(null=True, blank=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True, blank=True) # exercise alanını ForeignKey ile ilişkilendiriyorum

    def calculate_calories(self):
        if self.calories_per_minute is None:
            self.calories_per_minute = 0  # None kontrolü ve 0 ataması
        
        age_factor = 1
        if self.age_group == '<18':
            age_factor = 1.2
        elif self.age_group == '18-30':
            age_factor = 1.5
        elif self.age_group == '30<':
            age_factor = 1.3
        
        # YAŞ KATSAYISI
        # 18 yaş altı için 1.2 | 18-30 yaş arası için 1.5 | 30 yaş üzeri için 1.3

        gender_factor = 1.1 if self.gender == 'male' else 1.0
        # CİNSİYET KATSAYISI
        # Erkekler için 1.1, Kadınlar için ekstra katsayı yok direkt 1.0 
        
        total_calories = self.exercise_duration * self.calories_per_minute * age_factor * gender_factor # Kalori Hesaplama
        return round(total_calories, 2) # Sonuç 2 ondalık basamağa yuvarlanır (çok küsüratlı gösteriyordu bunu ekledim)
