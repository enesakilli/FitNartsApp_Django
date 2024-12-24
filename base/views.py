from django.shortcuts import render, redirect
from django.contrib.auth.models import User # Kullanıcı modeli: username password falan sağlıyor
from django.contrib.auth import authenticate, login, logout # Direkt kullanılabiliyor 
from django.contrib import messages # Flash Messages, işlemlerden sonra mesaj yazdırıp home kısmında bastıracağım (success, error vsvs)
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from .models import UserProfile

# Create your views here.

def register_user(request):
    if request.method == 'POST': # request.method = POST ise alttaki işlemler yapılır ve GET ile kullanıcıya form gösterilir
        username = request.POST['username'] # request.POST: Kullanıcıdan gelen veriler
        password = request.POST['password']

        if User.objects.filter(username = username).exists(): # User daha önce kayıtlı mı
            # User.objects.filter bunu kullanmak aklıma gelmiyor
            messages.error(request, 'User already exists') # Flash message
        else:
            User.objects.create_user(username = username, password = password) # create ile veritabanında username ve password bilgileri kullanılarak user oluşturulur
            messages.success(request, 'Registration successful')
            return redirect ('login') # Register olduktan sonra login e yolluyorum
    return render(request, 'base/register.html') # GET ise kullanıcıya form gösterilir 


def login_user(request): # Direkt def login diye kullanmadım import edilecek şeyler var karışmasın
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        # authenticate kimlik doğrulama yapıyor
        
        if user is not None: # Giriş başarılı mı
            login(request, user) # authentication modülünden geliyor, contrib.auth importlu kısımdan geliyor
            # messages.success(request, 'Login successful')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password') # Flash message
            return redirect ('login')
    return render(request, 'base/login.html')


def logout_user(request):
    logout(request) # Otomatik olarak yapar (contrib.auth importlu kısımdan geliyor)
    # messages.success(request, 'Successfully logged out')
    return redirect('login')


def home(request):
    if not request.user.is_authenticated: # Kullanıcının giriş yapmış mı kontrol ediyorum
        return redirect('login') # Giriş yapmamışsa logine yolluyorum
    return render(request, 'base/home.html') # Giriş yapmışsa Home sayfasına yollar 


@login_required
def edit_profile(request):
    user_profile = request.user.userprofile 
    # Giriş yapmış kullanıcının profil bilgilerini UserProfile modelinden alır böylece kullanıcı sadece kendi profil bilgilerini düzenleyebilir

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile) # Form oluşturuyorum bunun için FORMS.PY gerekiyor
        # instance --> user_profile adlı mevcut kullanıcı profil verisi, formu doldururken başlangıç değerlerini sağlamak için formun instance parametresine verilir
        # Yani, formda görüntülenecek alanlar, kullanıcı profilinden alınan verilerle önceden doldurulur
        # request.FILES unutma --> fotolar için
        if form.is_valid(): # UserProfileForm ile kullanıcı profil verilerini çekiyorum
            form.save()
            return redirect('profile') # Geçerliyse kaydedip profile sayfasına yolluyorum
        else:
            print("Form errors:", form.errors) # Form hatalarını yazdırır (Hata ayıklama için)
    else:
        form = UserProfileForm(instance=user_profile) # Kullanıcı profil bilgileriyle formu göster
        # instance -->  Django formunu bir model örneğiyle ilişkilendirmenizi sağlar
        # Yani bir formda verileri güncellemek istiyorsak, instance ile var olan nesneyi form ile ilişkilendiririz
    return render(request, 'base/edit_profile.html', {'form': form}) 


@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    # get_or_create metodu kullanıyoruz --> Bir kullanıcının profil verisi varsa getirir yoksa oluşturur
    # Kullanıcı için var olan bir profil verisini almak veya yoksa yeni bir profil oluşturmak için kullanılır
    
    context = {'user': request.user, 'profile': user_profile} # Kullanıcı ve profil bilgileri
    return render(request, 'base/profile.html', context)

    # return render(request, 'profile.html', {'user': request.user, 'profile': user_profile})