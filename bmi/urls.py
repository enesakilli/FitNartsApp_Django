from django.urls import path
from . import views

urlpatterns = [
    path('', views.health_calculator, name='health_calculator'), # '' yerine bmi yazarsan /bmi/bmi olur
]
