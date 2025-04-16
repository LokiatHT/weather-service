import os
import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

@csrf_exempt
def get_weather(request):
    city = request.GET.get('city')
    if not city:
        return JsonResponse({'error': 'City parameter is required'}, status=400)

    api_key = os.getenv('OPENWEATHER_API_KEY')
    if not api_key:
        return JsonResponse({'error': 'API key not found in environment'}, status=500)

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200:
            return JsonResponse({'error': data.get('message', 'Failed to fetch weather')}, status=response.status_code)

        weather_data = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
        }

        return JsonResponse(weather_data)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def home(request):
    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET['city']
        api_key = os.getenv('OPENWEATHER_API_KEY')

        if not api_key:
            return render(request, 'home.html', {'error': 'API key missing'})

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if data.get('cod') != 200:
                return render(request, 'home.html', {'error': 'City not found'})

            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
            }
            return render(request, 'home.html', {'weather': weather_info})

        except Exception as e:
            return render(request, 'home.html', {'error': str(e)})

    return render(request, 'home.html')
