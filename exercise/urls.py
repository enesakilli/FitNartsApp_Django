from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.exercise_list, name='exercise_list'), # '' yerine exercise yazarsan /exercise/exercise olur
    path('add/', views.add_exercise, name='add_exercise'),
    path('edit/<int:pk>/', views.edit_exercise, name='edit_exercise'),
    path('delete/<int:pk>', views.delete_exercise, name='delete_exercise'),
    path('<int:pk>/', views.exercise_detail, name='exercise_detail'), # exercise/<int:pk>/'yı değiştirdim exercise/exercise/23 oluyordu, artık exercise/23 oluyor
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)