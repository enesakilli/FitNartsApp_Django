from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name='home'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('profile/', views.profile, name='profile'),
] 

if settings.DEBUG: # Fotoğraflar için gerekli
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)