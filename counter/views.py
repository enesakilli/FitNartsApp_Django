from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from exercise.models import Exercise # exercise app'inden Exercise modelini import ettim
from .models import Activity
from django.utils.timezone import now
from .forms import ActivityForm
from django.http import JsonResponse # Safe parametresi için
from django.db.models import Sum

# Create your views here.

def counter_view(request):
    default_exercise_list = Exercise.objects.filter(user=None, is_default=True)  # Varsayılan egzersizler
    custom_exercise_list = Exercise.objects.filter(user=request.user, is_default=False)  # Kullanıcının eklediği egzersizler
    
    total_calories = None # Başlangıçta hesaplanmış kalori yok
    form = ActivityForm(request.POST or None, default_exercises=default_exercise_list, custom_exercises=custom_exercise_list)

    if not form.is_valid():
        print("### form errors:", form.errors)
    if request.method == 'POST':
        # Seçilen egzersize göre calories_per_minute'yi güncelle
        selected_exercise_id = form.cleaned_data.get('exercise_id') # Form verileri kullanıcıdan alındığında, Django bu verileri kontrol eder (Boş veya doğru türde olup olmadığını vsvs)
        form.set_calories_per_minute(selected_exercise_id) # Doğrulama işlemleri başarılı olduktan sonra cleaned_data içinde saklar
        activity = form.save(commit=False) # commit=False diyerek calculate e basınca hesaplama yapılacak ama veritabanına kaydedilmeyecek, save ile kaydedilecek
        activity.user = request.user  # Kullanıcıyı ekliyoruz

        total_calories = activity.calculate_calories() # Kalori hesaplama (models dosyasında)

        # None kontrolü ekledim None'u hesaplarken hata veriyordu
        if activity.calories_per_minute is None:
            activity.calories_per_minute = 0 # Varsayılan değer

        # Eğer Save butonuna basılmışsa hesaplanan kaloriyi kaydediyoruz
        if 'save' in request.POST and total_calories:
            activity.calories_burned = total_calories
            # messages.success(request, 'Exercise saved successfully')
            activity.save()
            
            # Refresh yapınca exercise ekleme olayı kalktı
            return redirect('counter_view') # PRG Deseni: Başarıyla işlem tamamlandıktan sonra yönlendirme
        
    # Template için context
    context = {
        "default_exercise_list": default_exercise_list,
        "custom_exercise_list": custom_exercise_list,
        "form": form,
        "total_calories": total_calories,
    }
    return render(request, 'counter/counter.html', context)


def chart_data(request):
    activities = (
        Activity.objects.filter(user=request.user, calories_per_minute__gt=0) # order.by ile son 10 kayıt gösterilir  
        # calories_per_minute__gt=0 --> Kalori değeri sıfırdan büyük olan aktiviteleri filtreler, 0 veya none olanları dahil etmiyorum
        .values("exercise__title")
        .annotate(total_calories=Sum("calories_burned"))
    )

    data = [
        {"category": activity["exercise__title"], "value": activity["total_calories"]} # NEDEN _ YERİNE __ KULLANDIK?
        for activity in activities
    ]
    return JsonResponse(data, safe=False)
    

def reset_chart(request):
    if request.method == "POST":
        Activity.objects.filter(user=request.user).delete() # Mevcut kullanıcının verilerini siler
        # messages.success(request, "Chart data has been reset")
        return redirect("counter_view")  # Grafiği gösteren sayfaya geri yönlendir

# JsonResponse kullanırken, safe parametresi JSON yanıtı oluştururken Python veri tipinin geçerliliğini kontrol eder
# safe=True (Varsayılan) --> JsonResponse sadece bir dictionary (context) döndürür 
# safe=False --> Dictionary (context) dışındaki veri tipleri (liste vs) döndürülebilir (şu an kullandığım liste)