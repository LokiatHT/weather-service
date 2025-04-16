import requests
from django.conf import settings

def fetch_weather_data(lat, lng):
    api_key = settings.OPENWEATHER_API_KEY
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}&units=metric"

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Weather API request failed.")

    data = response.json()
    return {
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }
