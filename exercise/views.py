from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Exercise

# Create your views here.
@login_required
def exercise_list(request):
    # exercise_list = Exercise.objects.all() # Her kullanıcıya exerciseleri ekliyor alttaki gibi yapmam lazım
    default_exercise_list = Exercise.objects.filter(is_default=True) # user=request.user i kaldırdım çünkü tüm kullanıcılara gözüksün istiyorum
    custom_exercise_list = Exercise.objects.filter(user=request.user, is_default=False) # Sadece giriş yapan kullanıcının eklediği exerciseler çekiliyor
    
    context = {
        "custom_exercise_list": custom_exercise_list,
        "default_exercise_list": default_exercise_list
    }
    return render(request, 'exercise/exercise_list.html', context) 


@login_required
def add_exercise(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        # 'cals_per_minute' değerini alırken boşluk kontrolü yapıyoruz
        cals_per_minute = request.POST.get('cals_per_minute', None)
        
        # Eğer cals_per_minute boş değilse, float'a çeviriyoruz
        if cals_per_minute == '':
            cals_per_minute = None # Eğer boşsa, hata almamak için None olarak ayarlıyoruz
        else:
            try:
                cals_per_minute = float(cals_per_minute) if cals_per_minute else None
            except ValueError:
                cals_per_minute = None # Eğer floata dönüştürme başarısız olursa None olarak ayarlıyoruz

        image = request.FILES.get('image')

        # Eğer image yüklenmemişse varsayılan image ayarlıyoruz
        if not image:
            image = 'images/no_image.png' # MEDIA_ROOT altındaki yol

        Exercise.objects.create( # create ile veritabanında exercise oluşturuyoruz
            user=request.user, # user = request.user --> Exercise'ı oturumu açmış olan kullanıcıyla eşleştiriyorum
            title=title, # title'ı Exercise için kaydediyorum 
            description=description,
            cals_per_minute=cals_per_minute,
            image=image
        )
        # messages.success(request, 'Exercise added successfully')
    return redirect('exercise_list')


@login_required
def edit_exercise(request, pk):
    exercise = Exercise.objects.filter(id=pk, user=request.user).first()
    # first() --> sorgu sonucu dönen veriler arasından ilk öğeyi alır.
    # Kullanıcının sahip olduğu belirli bir exercise'ı al

    if not exercise:  # Egzersiz bulunamazsa hata mesajı verir ve liste sayfasına yönlendirir
        messages.error(request, 'Exercise not found or you do not have permission to edit it.')
        return redirect('exercise_list')

    if request.method == 'POST': # exercise_add işlemi gibi aynı şeyleri yapıyoruz, yukarıda filtre ile belirli bir exercise seçeriz
        title = request.POST['title']
        description = request.POST['description']
        cals_per_minute = request.POST.get('cals_per_minute', None)
        image = request.FILES.get('image')

        # cals_per_minute kontrolü
        if cals_per_minute == '':
            cals_per_minute = None
        else:
            try:
                cals_per_minute = float(cals_per_minute) if cals_per_minute else None
            except ValueError:
                cals_per_minute = None

        # Exercise modelini güncelle
        exercise.title = title
        exercise.description = description
        exercise.cals_per_minute = cals_per_minute

        if image:  # Eğer yeni bir resim yüklenmişse, eski resmi günceller
            exercise.image = image

        exercise.save()  # Değişiklikleri kaydet
        # messages.success(request, 'Exercise updated successfully.')
        return redirect('exercise_list')

    # Formu doldurmak için mevcut egzersiz verileri
    context = {
        'exercise': exercise
    }
    return render(request, 'exercise/edit_exercise.html', context)


@login_required
def delete_exercise(request, pk): # primary key kullandım çünkü belirli seçilecek bir Exercise'ı silmem gerekli
    exercise = Exercise.objects.get(id = pk, user = request.user)
    # get ile veritabanından silinecek bir exercise alıyorum
    # pk kullanmam gerekli çünkü belirli bir exercise silinecek 
    # user = request.user ile exercise kontrolü yapılır (oturumu açan kişiye ait)
    
    if exercise:
        exercise.delete() # Exercise silinir ORM sayesinde
        # messages.success(request, 'Exercise deleted successfully')
    return redirect('exercise_list') 
    

@login_required
def exercise_detail(request, pk):
    exercise = Exercise.objects.filter(id = pk).first() # , user = request.user kaldırdım yoksa user request ediyor gözükmüyor
    # first() --> sorgu sonucu dönen veriler arasından ilk öğeyi alır.
    # Kullanıcının sahip olduğu belirli bir exercise'ı al
    
    if not exercise:  # Exercise yoksa kullanıcıyı ana sayfaya yönlendir
        messages.error(request, 'Exercise not found.')
        return redirect('home')
    return render(request, 'exercise/exercise_detail.html', {'exercise': exercise})
      