from . import views
from django.urls import path
from .views import multi_city_weather
from .views import get_weather
from .views import register_user

# urlpatterns = [
#     path('weather', get_weather),
#     path('weather/history', get_weather_history),
# ]



urlpatterns = [
    path('', views.home, name='home'),
    path('weather/', views.get_weather, name='get_weather'),
    path('weather/', get_weather, name='get_weather'),
    path('multi', multi_city_weather),
    path('register', register_user),
]



# weather/urls.py


