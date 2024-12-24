from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.counter_view, name='counter_view'), # '' yerine counter yazarsan /counter/counter olur
    path('chart/', views.chart_data, name='chart_data'),
    path('reset-chart/', views.reset_chart, name='reset_chart'),
]
