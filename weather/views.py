from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import SearchHistory, FavoriteCity
from .utils import get_weather_data, get_forecast_data, get_location_weather
from django.contrib.auth.models import User
from .forms import UserRegistrationForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    """Home page view with weather search functionality."""
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            weather_data = get_weather_data(city)
            if weather_data:
                # Save search history
                if request.user.is_authenticated:
                    SearchHistory.objects.create(
                        user=request.user,
                        city=city,
                        temperature=weather_data['main']['temp'],
                        description=weather_data['weather'][0]['description'],
                        humidity=weather_data['main']['humidity'],
                        wind_speed=weather_data['wind']['speed']
                    )
                
                # Get forecast data
                forecast_data = get_forecast_data(city)
                
                context = {
                    'weather': weather_data,
                    'forecast': forecast_data,
                    'city': city
                }
                return render(request, 'weather/index.html', context)
            else:
                messages.error(request, 'City not found. Please try again.')
    
    return render(request, 'weather/index.html')

@login_required
def add_favorite(request):
    """Add a city to user's favorites."""
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            FavoriteCity.objects.get_or_create(user=request.user, city=city)
            messages.success(request, f'{city} added to favorites!')
    return redirect('index')

@login_required
def remove_favorite(request):
    """Remove a city from user's favorites."""
    if request.method == 'POST':
        city = request.POST.get('city')
        if city:
            FavoriteCity.objects.filter(user=request.user, city=city).delete()
            messages.success(request, f'{city} removed from favorites!')
    return redirect('index')

@login_required
def favorites(request):
    """Display user's favorite cities."""
    favorites = FavoriteCity.objects.filter(user=request.user)
    weather_data = []
    
    for fav in favorites:
        data = get_weather_data(fav.city)
        if data:
            weather_data.append({
                'city': fav.city,
                'weather': data
            })
    
    return render(request, 'weather/favorites.html', {'weather_data': weather_data})

def get_location_weather_view(request):
    """Get weather data for user's current location."""
    if request.method == 'POST':
        lat = float(request.POST.get('lat'))
        lon = float(request.POST.get('lon'))
        
        weather_data = get_location_weather(lat, lon)
        if weather_data:
            return JsonResponse(weather_data)
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

def register(request):
    """Handle user registration with improved error handling."""
    if request.method == 'POST':
        try:
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                try:
                    user = form.save()
                    username = form.cleaned_data.get('username')
                    logger.info(f'Successfully created user account for {username}')
                    messages.success(request, f'Account created for {username}! You can now log in.')
                    return redirect('login')
                except Exception as e:
                    logger.error(f'Error saving user: {str(e)}')
                    messages.error(request, 'An error occurred while creating your account. Please try again.')
            else:
                logger.warning(f'Form validation errors: {form.errors}')
                messages.error(request, 'Please correct the errors below.')
        except Exception as e:
            logger.error(f'Unexpected error during registration: {str(e)}')
            messages.error(request, 'An unexpected error occurred. Please try again.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})
