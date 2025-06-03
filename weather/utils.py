import requests
from django.conf import settings
from typing import Dict, Any, Optional

def get_weather_data(city: str) -> Optional[Dict[str, Any]]:
    """
    Fetch current weather data for a given city using OpenWeatherMap API.
    """
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use metric units (Celsius)
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def get_forecast_data(city: str) -> Optional[Dict[str, Any]]:
    """
    Fetch 5-day weather forecast data for a given city using OpenWeatherMap API.
    """
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None

def get_location_weather(lat: float, lon: float) -> Optional[Dict[str, Any]]:
    """
    Fetch weather data for a given latitude and longitude using OpenWeatherMap API.
    """
    api_key = settings.OPENWEATHERMAP_API_KEY
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
        'units': 'metric'
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None 