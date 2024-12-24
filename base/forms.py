from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm): # UserProfile verilerini form aracılığıyla alacağız
    class Meta: # Meta sınıfı, formun özelliklerini tanımlar
        model = UserProfile # UserProfileForm formu, UserProfile modelinin verilerini kullanarak oluşturulacak
        fields = ['name', 'surname', 'gender', 'age', 'height', 'weight', 'profile_picture'] # Formda yer alacak alanlar