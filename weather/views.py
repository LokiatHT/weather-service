import os
import requests
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from .models import UserAPIKey


# Load environment variables from .env
load_dotenv()

@csrf_exempt
def register_user(request):
    if request.method == "POST":
        key = UserAPIKey.objects.create()
        return JsonResponse({"api_key": key.api_key})
    return JsonResponse({"error": "POST required"}, status=405)

def api_key_required(view_func):
    def wrapper(request, *args, **kwargs):
        api_key = request.headers.get("X-API-Key")
        if not api_key:
            return JsonResponse({"error": "API key required"}, status=403)

        try:
            user_key = UserAPIKey.objects.get(api_key=api_key)
            if not user_key.is_valid():
                return JsonResponse({"error": "API key usage limit exceeded"}, status=403)
            user_key.increment_usage()
        except UserAPIKey.DoesNotExist:
            return JsonResponse({"error": "Invalid API key"}, status=403)

        return view_func(request, *args, **kwargs)
    return wrapper

@csrf_exempt
@api_key_required
def multi_city_weather(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            cities = data.get("cities", [])
            results = []

            api_key = os.getenv("OPENWEATHER_API_KEY")

            for city in cities:
                response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
                if response.status_code == 200:
                    results.append(response.json())
                else:
                    results.append({"city": city, "error": "Not found"})
            
            return JsonResponse({"results": results})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "POST request required"}, status=405)

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
