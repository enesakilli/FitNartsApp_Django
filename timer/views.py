from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Timer
from django.utils.timezone import now

# Create your views here.

def timer_view(request):
    timer, created = Timer.objects.get_or_create(id=1)  
    # Veritabanında Timer modeli üzerinden id=1 olan bir nesneyi arar
    # Eğer bu id ile bir kayıt yoksa, yeni bir Timer nesnesi oluşturur ve veritabanına kaydeder
    # created --> Yeni bir nesne oluşturulmuşsa True, yoksa False döner
    # Yalnızca tek bir zamanlayıcı için çalışır. Bu nedenle id=1 kullanıldı

    elapsed_time = timer.elapsed_time # Toplam geçen süre
    if timer.is_running:
        elapsed_time += (now() - timer.start_time).total_seconds() 
        # timer.start_time --> Zamanlayıcının başlatıldığı anı tutar
        # now() --> Şu anki zamanı temsil eder
        # İkisi arasındaki fark, zamanlayıcının ne kadar süredir çalıştığını verir
        # total_seconds() --> Bu farkı saniye cinsinden ifade eder
        # elapsed_time += --> Bu süreyi mevcut elapsed_time değerine ekler. Böylece, zamanlayıcı çalışırken geçen süreyi de hesaba katar
        
    elapsed_minutes = int(elapsed_time // 60) # Toplam geçen süreden dakikaları bulur 
    elapsed_seconds = int(elapsed_time % 60) # Toplam geçen süreden geriye kalan saniyeleri bulur

    context = {
        "timer": timer,
        "elapsed_minutes": elapsed_minutes,
        "elapsed_seconds": elapsed_seconds,
    }    
    return render(request, 'timer/timer_view.html', context)


def start_timer(request):
    timer, created = Timer.objects.get_or_create(id=1)
    if not timer.is_running: # False ise
        timer.start_time = now() 
        # now() --> Şu anki zamanı alır, start time ile eşitleyerek zamanlayıcının başlama zamanını şu anki zamanla ayarlar
        timer.is_running = True # Zamanlayıcının çalışıp çalışmadığını tutar
        timer.save() # Yapılan değişiklikleri veritabanına kaydeder
    return redirect("timer_view")


def stop_timer(request):
    timer = Timer.objects.get(id=1)
    if timer.is_running:
        timer.elapsed_time += (now() - timer.start_time).total_seconds() # Geri kaldığı yerden devam etme
        timer.is_running = False # Zamanlayıcıyı durdurduğumuzda, zamanlayıcının durumunu False yapar
        timer.start_time = None # Zamanlayıcının durduğunda başlama zamanı olan start_time'ı None yapar
        # None --> zamanlayıcı tekrar başlatıldığında yeni bir başlangıç zamanı ayarlanabilmesi için gereklidir
        # Zamanlayıcı durdurulurken, elapsed_time'a geçen süre ekleniyor. Bu, zamanlayıcı durduğunda kaydedilen sürenin biriktiği anlamına gelir
        timer.save()
    return redirect("timer_view")


def reset_timer(request):
    timer = Timer.objects.get(id=1)
    timer.start_time = None
    timer.is_running = False
    timer.elapsed_time = 0.0 # elapsed_time'ı sıfırlar 
    timer.save()
    return redirect("timer_view")

# start_timer'da objects.get_or_create, stop_timer ve reset_timer'da sadece objects.get kullanılıyor
# get_or_create: Nesne bulunmazsa yeni bir tane oluşturur --> Start a basınca ekleniyor
# get: Yalnızca var olan nesneyi alır --> Nesne var olarak sayılıyor start'ın oluşturduğu
