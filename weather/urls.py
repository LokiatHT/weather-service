from . import views
from django.urls import path
from .views import get_weather

# urlpatterns = [
#     path('weather', get_weather),
#     path('weather/history', get_weather_history),
# ]



urlpatterns = [
    path('', views.home, name='home'),
    path('weather/', views.get_weather, name='get_weather'),
    path('weather/', get_weather, name='get_weather'),
    # path('weather/history/', views.get_weather_history, name='get_weather_history'),
]



# weather/urls.py


