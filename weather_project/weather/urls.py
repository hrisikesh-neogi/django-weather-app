from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_view, name='weather_view'),
    path('place/<str:city_name>/', views.place_info, name='place_info'), 
]
