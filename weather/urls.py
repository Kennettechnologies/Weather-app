from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('favorites/', views.favorites, name='favorites'),
    path('add-favorite/', views.add_favorite, name='add_favorite'),
    path('remove-favorite/', views.remove_favorite, name='remove_favorite'),
    path('get-location-weather/', views.get_location_weather_view, name='get_location_weather'),
    path('register/', views.register, name='register'),
] 