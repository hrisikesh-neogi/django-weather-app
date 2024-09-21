import requests
from django.shortcuts import render
from .forms import CityForm
from django.conf import settings
from opencage.geocoder import OpenCageGeocode
from .models import WeatherSearchHistory
from datetime import datetime
import os

# Function to get latitude and longitude for a given city using OpenCage API
def get_coordinates(city):
    geocode_api_key = os.getenv('GEOCODE_API_KEY')
    geocoder = OpenCageGeocode(geocode_api_key)

    results = geocoder.geocode(city)
    if len(results) > 0:
        
        return results
    return None

def weather_view(request):
    city = None
    weather_data = None
    error_message = None
    flag = None
    formatted_city = None
    search_history = WeatherSearchHistory.objects.all().order_by('-search_time')  # Fetch search history

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']

            # Get latitude and longitude for the city
            geo_results = get_coordinates(city)
            
            if geo_results:
                geo_data = geo_results[0]["geometry"]
                formatted_city = geo_results[0]["formatted"]
                lat = geo_data["lat"]
                lon = geo_data["lng"]
                flag = geo_results[0]["annotations"]["flag"]
                
                # Open-Meteo API URL
                url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true'
                response = requests.get(url)
                
                
                if response.status_code == 200:
                    weather_data = response.json()
                    
                    temperature = weather_data["current_weather"]["temperature"]  # For example
                    wind_speed = weather_data["current_weather"]["windspeed"]
                    wind_direction = weather_data["current_weather"]["winddirection"]  # Modify based on actual data
                    
                    WeatherSearchHistory.objects.create(
                            city=city,
                            temperature=temperature,
                            wind_speed=wind_speed,
                            wind_direction=wind_direction
                        )
                else:
                    error_message = "Couldn't fetch weather data. Please try again later."
            else:
                error_message = "City not found. Please try again."
    else:
        form = CityForm()

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    context = {
        'form': form,
        'country_flag':flag,
        'time': current_time,
        'city': formatted_city,
        'weather_data': weather_data,
        'error_message': error_message,
        'search_history': search_history  # Include search history in context for display in template.html  # Include search history in context for display in template.html  # Include search history in context for display in template.html  # Include search history in context for display in template.html  # Include search history in context for display in template.html  # Include search history in context for display in template.html  # Include search history in context for display in template.html
    }
    return render(request, 'weather/weather.html', context)
