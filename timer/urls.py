from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.timer_view, name='timer_view'), # '' yerine timer yazarsan /timer/timer olur
    path('start/', views.start_timer, name='start_timer'),
    path('stop/', views.stop_timer, name='stop_timer'),
    path('reset/', views.reset_timer, name='reset_timer'),
]
